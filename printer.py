from typing import List

from jinja2 import Environment, PackageLoader, select_autoescape

from IDLContext import IDLContext
from IDLModels import IDLMethodArgument, IDLMethod, IDLMethodArgumentDirection
from IDLTypes import IDLTypeStorage
from parser import parse_idl


def storage_args_filter(typ: IDLTypeStorage, inv: bool = False):
    return lambda args: filter(lambda i: (i.decl.type.storage == typ) ^ inv, args)


def dir_args_filter(typ: IDLMethodArgumentDirection):
    return lambda args: filter(lambda i: i.dir == typ, args)


class IdentifierPrinter:
    def __init__(self, ctx: IDLContext | None):
        self.ctx = ctx

    def print_method_argument(self, arg: IDLMethodArgument) -> str:
        type_cpp = str(arg.decl.type)
        if arg.decl.type.storage != IDLTypeStorage.VALUE:
            type_cpp = f"const {type_cpp}&"
        return f"{type_cpp} {arg.decl.name}"


class MethodPrinter:

    def __init__(self, ctx: IDLContext | None):
        self.ctx = ctx
        self.id_printer = IdentifierPrinter(self.ctx)

    def method_request_type(self, m: IDLMethod) -> str:
        return f"{self.ctx.fqn}_{m.name}_req"

    def method_response_type(self, m: IDLMethod) -> str:
        return f"{self.ctx.fqn}_{m.name}_res"

    def arguments(self, m: IDLMethod) -> List[str]:
        args = sorted(m.arguments, key=lambda x: x.dir)
        return [self.id_printer.print_method_argument(i) for i in args if i.dir == IDLMethodArgumentDirection.IN]

    def response_wrapper_name(self, m: IDLMethod):
        return f"{self.ctx.namespace}::{self.ctx.classname}::{m.name}Response"

    def return_type(self, m: IDLMethod) -> str:
        return f"const {self.response_wrapper_name(m)}&"


class InterfacePrinter:
    def __init__(self):
        self.env = Environment(
            loader=PackageLoader("printer"),
            autoescape=select_autoescape()
        )
        self.env.filters["arena_args"] = storage_args_filter(IDLTypeStorage.ARENA)
        self.env.filters["fixed_args"] = storage_args_filter(IDLTypeStorage.ARENA, True)
        self.env.filters["in_args"] = dir_args_filter(IDLMethodArgumentDirection.IN)
        self.env.filters["out_args"] = dir_args_filter(IDLMethodArgumentDirection.OUT)
        self.template_header = self.env.get_template("idl.hpp.jinja")
        self.template_source = self.env.get_template("idl.cpp.jinja")

    def process(self, ctx: IDLContext, target_dir: str):
        self.env.globals["method_printer"] = MethodPrinter(ctx)
        self.env.globals["id_printer"] = IdentifierPrinter(ctx)

        data = dict(
            ctx=ctx,
            ns=ctx.namespace,
            cls=ctx.classname,
            methods=ctx.interface.methods
        )
        header = self.template_header.render(data)
        source = self.template_source.render(data)

        base_path = f"{target_dir}/{ctx.namespace}/{ctx.classname}"
        with open(f"{base_path}.idl.hpp", "w") as f:
            f.write(header)
        with open(f"{base_path}.idl.cpp", "w") as f:
            f.write(source)


if __name__ == "__main__":
    idl_file = "/home/petr/CLionProjects/trafficlight/resources/idl/ILightMode.idl"
    out_dir = "/home/petr/CLionProjects/trafficlight/tl_control/src"

    idl_ctx = parse_idl(idl_file)

    for m in idl_ctx.interface.methods:
        l = '\n\t'.join(
            map(lambda arg: f"{arg.name}:\t{arg.dir.name}\t{arg.decl.type.storage.name}\t{arg.decl.type}",
                m.arguments))
        print(f"{m.name}(\n\t{l}\n)")

    printer = InterfacePrinter()
    printer.process(idl_ctx, out_dir)
