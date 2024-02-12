from dataclasses import dataclass
from enum import StrEnum
from typing import List, Callable


class IDLMethodArgumentDirection(StrEnum):
    IN = 'in'
    OUT = 'out'
    ERROR = 'error'


@dataclass
class IDLIdentifier:
    name: str


@dataclass
class IDLDeclaration:
    type: IDLIdentifier
    name: str


@dataclass
class IDLMethodArgument:
    dir: IDLMethodArgumentDirection
    decl: IDLDeclaration

    @property
    def name(self):
        return self.decl.name


@dataclass
class IDLMethod:
    name: str
    arguments: List[IDLMethodArgument]

    def get_args(self, dir: IDLMethodArgumentDirection) -> List[IDLMethodArgument]:
        return [i for i in self.arguments if i.dir == dir]

    @property
    def in_args(self) -> List[IDLMethodArgument]:
        return self.get_args(IDLMethodArgumentDirection.IN)

    @property
    def out_args(self) -> List[IDLMethodArgument]:
        return self.get_args(IDLMethodArgumentDirection.OUT)


@dataclass
class IDLInterface:
    name: str
    methods: List[IDLMethod]


@dataclass
class IDLContext:
    namespace: str
    classname: str
    interface: IDLInterface

    def __post_init__(self):
        self.namespace = self._translate_separators(self.namespace)
        self.classname = self._translate_separators(self.classname)

    @staticmethod
    def _translate_separators(x: str) -> str:
        return x.replace(".", "_")

    @property
    def fqn(self) -> str:
        return f"{self.namespace}_{self.classname}"
