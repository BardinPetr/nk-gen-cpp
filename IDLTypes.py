from dataclasses import dataclass
from enum import StrEnum, Enum
from typing import Dict, Optional


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
    resolves: 'IDLType'
    storage: IDLTypeStorage = IDLTypeStorage.VALUE


@dataclass
class IDLTypeStruct(IDLType):
    name: str
    children: Dict[str, IDLType]


@dataclass
class IDLTypeTypeDef(IDLType):
    name: str
    children: IDLType


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


@dataclass
class IDLTypeList(IDLType):
    container: IDLTypeContainerPrimitive
    element: IDLType

    def __str__(self):
        return f"vector<{self.element}>"
