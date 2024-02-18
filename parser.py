from typing import Optional

from antlr4 import *

from IDLContext import IDLContext
from IDLModels import *
from IDLTypes import *

from antlr.IDLListener import *
from antlr.IDLLexer import *
from antlr.IDLParser import *
from antlr.IDLVisitor import IDLVisitor


class InterfaceBuilderVisitor(IDLVisitor):

    def aggregateResult(self, aggregate, nextResult):
        """
        Overrides internal aggregation function to return children parse results as list
        Ignores children which returned None
        """
        if aggregate is None:
            aggregate = []
        if nextResult is None:
            return aggregate
        return aggregate + [nextResult]

    def visitStatement_import(self, ctx: IDLParser.Statement_importContext):
        print("Imports are not supported")
        exit(1)

    def visitStatement_union(self, ctx: IDLParser.Statement_unionContext):
        print("Unions are not supported")
        exit(1)

    def visitIdl(self, ctx: IDLParser.IdlContext):
        # parse package name
        package = ctx.statement_package().PACKAGE_ID().getText()
        packages = package.split('.')
        namespace, classname = '.'.join(packages[:-1]), packages[-1]
        print(f"Processing interface {classname} of package {namespace}")

        # parse typedefs
        typedefs = {}
        consts = {}
        for i in ctx.statements().statement():
            definition = self.visit(i)[0]
            if isinstance(definition, IDLTypeStruct | IDLTypeTypeDef):
                typedefs[definition.name] = definition
            if isinstance(definition, IDLConst):
                consts[definition.name] = definition

        # parse single interface
        interface = self.visit(ctx.interface())
        interface.name = classname
        return IDLContext(namespace, classname, interface, typedefs, consts)

    def visitInterface(self, ctx: IDLParser.InterfaceContext):
        methods = self.visit(ctx.method_block())
        return IDLInterface("", methods)

    def visitMethod(self, ctx: IDLParser.MethodContext):
        return IDLMethod(
            name=ctx.ID().getText(),
            arguments=self.visit(ctx.method_arguments())
        )

    def visitMethod_argument(self, ctx: IDLParser.Method_argumentContext):
        return IDLMethodArgument(
            dir=IDLMethodArgumentDirection(ctx.ARG_DIRECTION().getText()),
            decl=self.visit(ctx.declaration())
        )

    def visitDeclaration(self, ctx: IDLParser.DeclarationContext):
        resolved_type: IDLType = self.visit(ctx.type_())
        return IDLDeclaration(
            type=resolved_type,
            name=ctx.ID().getText()
        )

    def visitType(self, ctx: IDLParser.TypeContext) -> Optional[IDLType]:
        if ct := ctx.ID():
            return IDLTypeID(ct.getText())
        if ct := ctx.TYPE_PRIMITIVE():
            return IDLTypePrimitive[ct.getText()]
        if ct := ctx.type_arr():
            base = IDLTypeContainerPrimitive[ct.TYPE_ARR().getText().capitalize()]
            if base == IDLTypeContainerPrimitive.String:
                return IDLTypeString()
            return IDLTypeList(base, IDLTypePrimitive.UInt8)
        if ct := ctx.type_arr_generic():
            resolved_type = self.visit(ct.type_())
            return IDLTypeList(
                IDLTypeContainerPrimitive[ct.TYPE_ARR_GENERIC().getText().capitalize()],
                resolved_type
            )
        return None

    def visitStatement_typedef(self, ctx: IDLParser.Statement_typedefContext) -> IDLType:
        return IDLTypeTypeDef(ctx.ID().getText(), self.visit(ctx.type_()))

    def visitStatement_struct(self, ctx: IDLParser.Statement_structContext) -> IDLType:
        declarations = self.visit(ctx.declaration_block())
        if not declarations:
            declarations = []
        declarations = {i.name: i.type for i in declarations}
        return IDLTypeStruct(ctx.ID().getText(), declarations)

    def visitStatement_const(self, ctx: IDLParser.Statement_constContext) -> IDLConst:
        c_type: IDLParser.Const_typeContext = ctx.const_type()
        if c_id := c_type.TYPE_PRIMITIVE():
            idl_type = IDLTypePrimitive[c_id.getText()]
        else:
            idl_type = IDLTypeID(c_type.ID().getText())

        return IDLConst(
            name=ctx.ID().getText(),
            type=idl_type,
            value=int(ctx.INT().getText())
        )


def parse_idl(path: str) -> IDLContext:
    fs = FileStream(path)
    lexer = IDLLexer(fs)
    tokens = CommonTokenStream(lexer)
    tree = IDLParser(tokens).idl()

    v = InterfaceBuilderVisitor()
    ctx = v.visit(tree)

    return ctx


if __name__ == '__main__':
    idl_file = "/home/petr/CLionProjects/trafficlight/resources/idl/ILightMode.idl"
    res = parse_idl(idl_file)
    print(res)
