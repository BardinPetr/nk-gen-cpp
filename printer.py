from jinja2 import Environment, PackageLoader, select_autoescape

from IDLModels import *
from parser import parse_idl

TYPES_PRIMITIVE = {f"{u}Int{i}" for u in ["S", "U"] for i in [8, 16, 32, 64]}
TYPES_ARRAY = {"bytes", "string"}
TYPES_ARRAY_GENERIC = {"bytes", "string"}
TYPES_POINTER = {*TYPES_ARRAY, *TYPES_ARRAY_GENERIC}
TYPES_INTERNAL = {*TYPES_PRIMITIVE, *TYPES_POINTER}


class IdentifierPrinter:
    def __init__(self, ctx: IDLContext | None):
        self.ctx = ctx

    def print_type_cpp(self, i: IDLIdentifier):
        name = i.name
        if name in TYPES_PRIMITIVE:
            return f"nk_{name.lower()}_t"
        return f"{self.ctx.fqn}_{i.name}"

    def print_decl(self, decl: IDLDeclaration) -> str:
        return f"{decl.type.name} {decl.name}"

    def print_method_argument(self, arg: IDLMethodArgument) -> str:
        type_name = arg.decl.type.name
        type_cpp = self.print_type_cpp(arg.decl.type)

        # use references for anything except integers
        if type_name not in TYPES_PRIMITIVE:
            type_cpp = f"const {type_cpp}&"

        return f"{type_cpp} {arg.decl.name}"


class MethodPrinter:

    def __init__(self, ctx: IDLContext | None):
        self.ctx = ctx
        self.id_printer = IdentifierPrinter(self.ctx)

    def return_type(self, m: IDLMethod) -> str:
        return f"const {self.method_response_type(m)}*"

    @property
    def request_type(self) -> str:
        return f"{self.ctx.fqn}_req"

    @property
    def response_type(self) -> str:
        return f"{self.ctx.fqn}_res"

    def method_request_type(self, m: IDLMethod) -> str:
        return f"{self.ctx.fqn}_{m.name}_req"

    def method_response_type(self, m: IDLMethod) -> str:
        return f"{self.ctx.fqn}_{m.name}_res"

    def in_args(self, m: IDLMethod) -> List[str]:
        return [self.id_printer.print_method_argument(i)
                for i in m.get_args(IDLMethodArgumentDirection.IN)]


class InterfacePrinter:
    def __init__(self):
        self.env = Environment(
            loader=PackageLoader("printer"),
            autoescape=select_autoescape()
        )
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

    printer = InterfacePrinter()
    printer.process(idl_ctx, out_dir)
