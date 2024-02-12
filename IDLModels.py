from dataclasses import dataclass
from enum import StrEnum
from typing import List, Optional, Dict

from IDLTypes import IDLType


@dataclass
class IDLConst:
    name: str
    type: IDLType
    value: int


class IDLMethodArgumentDirection(StrEnum):
    IN = 'in'
    OUT = 'out'
    ERROR = 'error'


@dataclass
class IDLDeclaration:
    type: IDLType
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
    interface: Optional[IDLInterface]
    typedefs: Dict[str, IDLType]
    consts: Dict[str, IDLConst]

    def __post_init__(self):
        self.namespace = self._translate_separators(self.namespace)
        self.classname = self._translate_separators(self.classname)
        self._compile_typedefs()

    @staticmethod
    def _translate_separators(x: str) -> str:
        return x.replace(".", "_")

    @property
    def fqn(self) -> str:
        return f"{self.namespace}_{self.classname}"

    def resolve_type(self, search: IDLType) -> IDLType:
        if self.typedefs is None: return search

        next_name = self.typedefs.get(str(search), None)
        if next_name is not None:
            return self.resolve_type(next_name)
        return search

    def _compile_typedefs(self):
        pass
