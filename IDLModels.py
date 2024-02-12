from dataclasses import dataclass
from enum import StrEnum
from typing import List, Optional, Dict

from IDLTypes import IDLType, IDLTypeID, IDLTypeList, IDLTypeStruct, IDLTypeTypeDef


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
        self._resolve_identifiers()

    @staticmethod
    def _translate_separators(x: str) -> str:
        return x.replace(".", "_")

    @property
    def fqn(self) -> str:
        return f"{self.namespace}_{self.classname}"

    def resolve_types(self, root: IDLType) -> IDLType:
        """
        Recursively resolve all ID types to definitions.
        Use by replacing target type with return value of function.
        """
        if isinstance(root, IDLTypeID) and root.name in self.typedefs:
            root = self.resolve_types(self.typedefs[root.name])

        elif isinstance(root, IDLTypeTypeDef):
            root = self.resolve_types(root.children)

        elif isinstance(root, IDLTypeList):
            root.element = self.resolve_types(root.element)

        elif isinstance(root, IDLTypeStruct):
            root.children = {n: self.resolve_types(t) for n, t in root.children.items()}

        return root

    def _resolve_identifiers(self):
        for m in self.interface.methods:
            for arg in m.arguments:
                arg.decl.type.resolves = self.resolve_types(arg.decl.type)
