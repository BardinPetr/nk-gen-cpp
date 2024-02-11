from dataclasses import dataclass, field
from typing import Dict, List, Optional

from jinja2 import Environment, PackageLoader, select_autoescape


@dataclass
class IDLContext:
    namespace: str = ""
    classname: str = ""
    separator: str = "_"

    @property
    def fqn(self):
        return self.separator.join(i for i in [self.namespace, self.classname] if i)

    @property
    def prefix(self):
        return (self.fqn + self.separator) if self.fqn else ""


@dataclass
class IDLType:
    INTERNAL_TYPES = {"UInt8", "UInt32"}
    PRIMITIVE_TYPES = {"UInt8", "UInt32"}

    name: str

    def render(self, ctx: IDLContext):
        if self.is_internal:
            return f"nk_{self.name.lower()}_t"
        return ctx.prefix + self.name

    @property
    def is_internal(self):
        return self.name in IDLType.INTERNAL_TYPES

    @property
    def is_primitive(self):
        return self.name in IDLType.INTERNAL_TYPES


@dataclass
class InterfaceParameterDefinition:
    type: str
    name: str
    ctx: IDLContext = field(default_factory=IDLContext)

    def __post_init__(self):
        self.idl_type = IDLType(self.type)

    def __str__(self):
        typename = self.idl_type.render(self.ctx)
        return (f"{typename} " if self.idl_type.is_primitive else f"const {typename} &") + self.name


@dataclass
class InterfaceMethodDefinition:
    name: str
    arg_in: List[InterfaceParameterDefinition]
    arg_out: List[InterfaceParameterDefinition]
    ctx: IDLContext = field(default_factory=IDLContext)

    def set_context(self, ctx: IDLContext):
        self.ctx = ctx
        for i in [*self.arg_in, *self.arg_out]:
            i.ctx = ctx

    @property
    def fqn(self):
        return f"{self.ctx.prefix}{self.name}"

    @property
    def req_type(self):
        return f"{self.fqn}_req"

    @property
    def res_type(self):
        return f"{self.fqn}_res"


@dataclass
class InterfaceDefinition:
    namespace: str
    name: str
    methods: List[InterfaceMethodDefinition]

    def __post_init__(self):
        ctx = IDLContext(self.namespace, self.name)
        for i in self.methods:
            i.set_context(ctx)

    @property
    def fqn(self):
        return f"{self.namespace}_{self.name}"


class InterfacePrinter:
    def __init__(self):
        self.env = Environment(
            loader=PackageLoader("nkx"),
            autoescape=select_autoescape()
        )

        self.template_header = self.env.get_template("idl.hpp.jinja")
        self.template_source = self.env.get_template("idl.cpp.jinja")

    def process(self, interface: InterfaceDefinition, target_dir: str):
        header = self.template_header.render(
            ns=interface.namespace,
            cls=interface.name,
            methods=interface.methods
        )
        source = self.template_source.render(
            ns=interface.namespace,
            cls=interface.name,
            interface=interface,
            methods=interface.methods
        )

        base_path = f"{target_dir}/{interface.namespace}/{interface.name}"
        open(f"{base_path}.idl.hpp", "w").write(header)
        open(f"{base_path}.idl.cpp", "w").write(source)


idf = InterfaceDefinition(
    'trafficlight',
    'ILightMode',
    [
        InterfaceMethodDefinition(
            "SetMode",
            [
                InterfaceParameterDefinition("CrossedDirectionsMode", "mode"),
                InterfaceParameterDefinition("UInt8", "par"),
            ],
            [],
        ),
        # InterfaceMethodDefinition(
        #     "methodA",
        #     [InterfaceParameterDefinition("UInt8", "in1"),InterfaceParameterDefinition("DirectionMode", "out1")],
        #     []
        # ),
        # InterfaceMethodDefinition(
        #     "methodB",
        #     [InterfaceParameterDefinition("UInt8", "in1"), InterfaceParameterDefinition("DirectionColor", "in2")],
        #     [InterfaceParameterDefinition("UInt8", "out1")],
        # ),
        # InterfaceMethodDefinition(
        #     "methodC",
        #     [InterfaceParameterDefinition("UInt8", "in1")],
        #     [InterfaceParameterDefinition("DirectionColor", "out1"), InterfaceParameterDefinition("UInt8", "out2")],
        # ),
    ]
)

InterfacePrinter().process(idf, "/home/petr/CLionProjects/trafficlight/tl_control/src")
