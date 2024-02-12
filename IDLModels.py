from dataclasses import dataclass
from enum import StrEnum
from typing import List


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


@dataclass
class IDLMethod:
    name: IDLIdentifier
    arguments: List[IDLMethodArgument]


@dataclass
class IDLInterface:
    name: str
    methods: List[IDLMethod]


@dataclass
class IDLContext:
    namespace: str
    classname: str
    interface: IDLInterface
