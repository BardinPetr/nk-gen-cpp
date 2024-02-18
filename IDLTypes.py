from dataclasses import dataclass
from enum import StrEnum, Enum
from typing import Dict


class IDLTypeContainerPrimitive(StrEnum):
    Bytes = "bytes"
    String = "string"
    Array = "array"
    Sequence = "sequence"


class IDLTypeStorage(Enum):
    VALUE = 1
    REFERENCE = 2
    ARENA = 3


class IDLType:
    def __init__(self):
        self.original: 'IDLType' = self
        self.storage: IDLTypeStorage = IDLTypeStorage.VALUE


@dataclass
class IDLTypeStruct(IDLType):
    name: str
    children: Dict[str, IDLType]

    def __post_init__(self):
        self.storage = IDLTypeStorage.REFERENCE

    def __str__(self):
        return self.name


@dataclass
class IDLTypeTypeDef(IDLType):
    name: str
    children: IDLType


@dataclass
class IDLTypeID(IDLType):
    name: str

    def __str__(self):
        return self.name


class IDLTypePrimitive(StrEnum):
    UInt8 = "nk_uint8_t"
    UInt16 = "nk_uint16_t"
    UInt32 = "nk_uint32_t"
    UInt64 = "nk_uint64_t"
    SInt8 = "nk_sint8_t"
    SInt16 = "nk_sint16_t"
    SInt32 = "nk_sint32_t"
    SInt64 = "nk_sint64_t"
    Handle = "Handle"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.storage = IDLTypeStorage.VALUE

    def __str__(self):
        return self.value


@dataclass
class IDLTypeString(IDLType):
    storage = IDLTypeStorage.ARENA
    def __str__(self):
        return "std::string"


@dataclass
class IDLTypeList(IDLType):
    container: IDLTypeContainerPrimitive
    element: IDLType
    storage = IDLTypeStorage.ARENA

    def __str__(self):
        return f"vector<{self.element}>"
