from dataclasses import dataclass
from enum import StrEnum
from typing import Dict


class IDLTypeContainerPrimitive(StrEnum):
    Bytes = "bytes"
    String = "string"
    Array = "array"
    Sequence = "sequence"


class IDLType:
    pass


@dataclass
class IDLTypeStruct(IDLType):
    children: Dict[str, IDLType]


@dataclass
class IDLTypeTypeDef(IDLType):
    name: str
    children: IDLType


@dataclass
class IDLTypeStruct(IDLType):
    name: str
    children: Dict[str, IDLType]


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
class IDLListType(IDLType):
    container: IDLTypeContainerPrimitive
    element: IDLType

    def __str__(self):
        return f"vector<{self.element}>"