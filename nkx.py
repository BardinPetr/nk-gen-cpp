from dataclasses import dataclass
from typing import Dict, List, Optional

from jinja2 import Environment, PackageLoader, select_autoescape


@dataclass
class InterfaceParameterDefinition:
    type: str
    name: str

    def __str__(self):
        return f"{self.type} {self.name}"


@dataclass
class InterfaceMethodDefinition:
    name: str
    arg_in: List[InterfaceParameterDefinition]
    arg_out: List[InterfaceParameterDefinition]
    parent: Optional["InterfaceDefinition"] = None

    @property
    def fqn(self):
        return f"{self.parent.fqn}_{self.name}"

    @property
    def req_fqn(self):
        return f"{self.fqn}_req"

    @property
    def res_fqn(self):
        return f"{self.fqn}_res"

    @property
    def res_type(self):
        return f"{self.res_fqn}*"


@dataclass
class InterfaceDefinition:
    namespace: str
    name: str
    methods: List[InterfaceMethodDefinition]

    def __post_init__(self):
        for i in self.methods:
            i.parent = self

    @property
    def fqn(self):
        return f"{self.namespace}_{self.name}"


class InterfacePrinter:
    def __init__(self, interface: InterfaceDefinition):
        self.interface = interface

        self.env = Environment(
            loader=PackageLoader("nkx"),
            autoescape=select_autoescape()
        )

        self.template_header = self.env.get_template("idl.hpp.jinja")
        self.template_source = self.env.get_template("idl.cpp.jinja")

        b = "/home/petr/CLionProjects/trafficlight/tl_control/src"

        header = self.template_header.render(
            ns=self.interface.namespace,
            cls=self.interface.name,
            methods=self.interface.methods
        )
        open(f"{b}/ILightMode.idl.hpp", "w").write(header)

        source = self.template_source.render(
            ns=self.interface.namespace,
            cls=self.interface.name,
            interface=self.interface,
            methods=self.interface.methods
        )
        open(f"{b}/ILightMode.idl.cpp", "w").write(source)


idf = InterfaceDefinition(
    'trafficlight',
    'ILightMode',
    [
        # InterfaceMethodDefinition(
        #     "GetMode",
        #     [],
        #     [InterfaceParameterDefinition("ABC", "abc")],
        # ),
        # InterfaceMethodDefinition(
        #     "SetMode",
        #     [InterfaceParameterDefinition("CrossedDirectionsMode", "mode")],
        #     [],
        # ),
        InterfaceMethodDefinition(
            "SetMode",
            [InterfaceParameterDefinition("CrossedDirectionsMode", "mode")],
            [],
        )
    ]
)

InterfacePrinter(idf)
