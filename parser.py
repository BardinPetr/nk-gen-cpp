from antlr4 import *

from IDLModels import *

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

    def visitIdl(self, ctx: IDLParser.IdlContext):
        # parse package name
        package = ctx.statement_package().PACKAGE_ID().getText()
        packages = package.split('.')
        namespace, classname = '.'.join(packages[:-1]), packages[-1]
        print(f"Processing interface {classname} of package {namespace}")

        interface: IDLInterface = self.visit(ctx.interface())
        interface.name = classname

        return IDLContext(
            namespace=namespace,
            classname=classname,
            interface=interface
        )

    def visitInterface(self, ctx: IDLParser.InterfaceContext):
        methods = self.visit(ctx.method_block())
        return IDLInterface("", methods)

    def visitMethod(self, ctx: IDLParser.MethodContext):
        return IDLMethod(
            name=IDLIdentifier(ctx.ID().getText()),
            arguments=self.visit(ctx.method_arguments())
        )

    def visitMethod_argument(self, ctx: IDLParser.Method_argumentContext):
        return IDLMethodArgument(
            dir=IDLMethodArgumentDirection(ctx.ARG_DIRECTION().getText()),
            decl=self.visit(ctx.declaration())
        )

    def visitDeclaration(self, ctx: IDLParser.DeclarationContext):
        return IDLDeclaration(
            type=IDLIdentifier(ctx.ID().getText()),
            name=ctx.type_().getText()
        )


def main(argv):
    idl_file = "/home/petr/CLionProjects/trafficlight/resources/idl/ILightMode.idl"

    fs = FileStream(idl_file)
    lexer = IDLLexer(fs)
    tokens = CommonTokenStream(lexer)
    tree = IDLParser(tokens).idl()

    v = InterfaceBuilderVisitor()
    interface = v.visit(tree)
    print(interface)


if __name__ == '__main__':
    main(sys.argv)
