from dataclasses import dataclass
from typing import Optional, Dict

from IDLModels import IDLInterface, IDLConst
from IDLTypes import IDLType, IDLTypeStruct, IDLTypeStorage, IDLTypeList, IDLTypeID, IDLTypeTypeDef


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

    def resolve_storage(self, root: IDLType) -> IDLTypeStorage:
        """
        Recursively check subtypes of given type to decide how it should be stored.
        If type is or has at least one 'array' type/subtype then whole tree gets IDLTypeStorage.ARENA
        Else primitives gets "VALUE", structures gets "REFERENCE"
        """
        if isinstance(root, IDLTypeStruct):
            if any(self.resolve_storage(i) == IDLTypeStorage.ARENA for i in root.children.values()):
                return IDLTypeStorage.ARENA
            return IDLTypeStorage.REFERENCE

        return root.storage

    def _resolve_identifiers(self):
        for m in self.interface.methods:
            m.arguments.sort(key=lambda x: x.dir)
            for arg in m.arguments:
                new_type = self.resolve_types(arg.decl.type)
                new_type.original = arg.decl.type
                arg.decl.type = new_type
                arg.decl.type.storage = self.resolve_storage(new_type)
