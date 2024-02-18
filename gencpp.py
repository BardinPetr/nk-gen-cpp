import re
import sys
from typing import List

from jinja2 import Environment, PackageLoader, select_autoescape

from IDLContext import IDLContext
from IDLModels import IDLMethodArgument, IDLMethod, IDLMethodArgumentDirection
from IDLTypes import IDLTypeStorage
from parser import parse_idl


def prettify(text: str) -> str:
    return re.sub(r"\n{2,}", "\n", text)


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
        return f"{type_cpp} {arg.fqn}"


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
        return f"nk_err_t"

    def request_args_initializers(self, a: List[IDLMethodArgument]):
        return [("{}" if i.type.storage == IDLTypeStorage.ARENA else i.fqn) for i in a]


class InterfacePrinter:
    def __init__(self):
        self.env = Environment(
            loader=PackageLoader("gencpp"),
            autoescape=select_autoescape()
        )
        self.env.filters["type"] = lambda x: type(x).__name__
        self.env.filters["arena_args"] = storage_args_filter(IDLTypeStorage.ARENA)
        self.env.filters["fixed_args"] = storage_args_filter(IDLTypeStorage.ARENA, True)
        self.env.filters["in_args"] = dir_args_filter(IDLMethodArgumentDirection.IN)
        self.env.filters["out_args"] = dir_args_filter(IDLMethodArgumentDirection.OUT)
        self.template_header = self.env.get_template("idl.hpp.jinja")
        self.template_source = self.env.get_template("idl.cpp.jinja")

    def process(self, ctx: IDLContext, target_dir: str):
        self.env.globals["method_printer"] = MethodPrinter(ctx)
        self.env.globals["id_printer"] = IdentifierPrinter(ctx)
        self.env.globals["ctx"] = ctx

        data = dict(
            ns=ctx.namespace,
            cls=ctx.classname,
            methods=ctx.interface.methods
        )

        header = self.template_header.render(data)
        source = self.template_source.render(data)

        header = prettify(header)
        source = prettify(source)

        with open(f"{target_dir}/include/{ctx.classname}.idl.hpp", "w") as f:
            f.write(header)
        with open(f"{target_dir}/src/{ctx.classname}.idl.cpp", "w") as f:
            f.write(source)

    @staticmethod
    def debug(ctx: IDLContext):
        for m in ctx.interface.methods:
            l = '\n\t'.join(
                map(lambda arg: f"{arg.name}:\t{arg.dir.name}\t{arg.decl.type.storage.name}\t{arg.decl.type}",
                    m.arguments))
            print(f"{m.name}(\n\t{l}\n)")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: printer.py <idl file> <target directory>")
        exit(1)

    idl_file, out_dir = sys.argv[1:]

    idl_ctx = parse_idl(idl_file)

    printer = InterfacePrinter()
    printer.process(idl_ctx, out_dir)
    printer.debug(idl_ctx)
