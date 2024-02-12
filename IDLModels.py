from dataclasses import dataclass
from enum import StrEnum
from typing import List, Callable, Dict


class IDLType:
    pass


@dataclass
class IDLTypeID(IDLType):
    name: str

    def __str__(self):
        return self.name


class IDLTypePrimitive(IDLType, StrEnum):
    UInt8 = "nk_uint8_t"
    UInt16 = "nk_uint16_t"
    UInt32 = "nk_uint32_t"
    UInt64 = "nk_uint64_t"
    SInt8 = "nk_sint8_t"
    SInt16 = "nk_sint16_t"
    SInt32 = "nk_sint32_t"
    SInt64 = "nk_sint64_t"
    Handle = "Handle"

    def __str__(self):
        return self.value


class IDLTypeContainerPrimitive(StrEnum):
    Bytes = "bytes"
    String = "string"
    Array = "array"
    Sequence = "sequence"


@dataclass
class IDLListType(IDLType):
    container: IDLTypeContainerPrimitive
    element: IDLType


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
    interface: IDLInterface
    typedefs: Dict[str, str]

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

    def resolve_type(self, typename: str):
        next_name = self.typedefs.get(typename, None)
        if next_name:
            return self.resolve_type(next_name)
        return typename

    def _compile_typedefs(self):
        pass
