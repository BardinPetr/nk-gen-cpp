# Generated from /home/petr/Desktop/nk-cpp/grammar/IDL.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .IDLParser import IDLParser
else:
    from IDLParser import IDLParser

# This class defines a complete listener for a parse tree produced by IDLParser.
class IDLListener(ParseTreeListener):

    # Enter a parse tree produced by IDLParser#idl.
    def enterIdl(self, ctx:IDLParser.IdlContext):
        pass

    # Exit a parse tree produced by IDLParser#idl.
    def exitIdl(self, ctx:IDLParser.IdlContext):
        pass


    # Enter a parse tree produced by IDLParser#interface.
    def enterInterface(self, ctx:IDLParser.InterfaceContext):
        pass

    # Exit a parse tree produced by IDLParser#interface.
    def exitInterface(self, ctx:IDLParser.InterfaceContext):
        pass


    # Enter a parse tree produced by IDLParser#statements.
    def enterStatements(self, ctx:IDLParser.StatementsContext):
        pass

    # Exit a parse tree produced by IDLParser#statements.
    def exitStatements(self, ctx:IDLParser.StatementsContext):
        pass


    # Enter a parse tree produced by IDLParser#statement.
    def enterStatement(self, ctx:IDLParser.StatementContext):
        pass

    # Exit a parse tree produced by IDLParser#statement.
    def exitStatement(self, ctx:IDLParser.StatementContext):
        pass


    # Enter a parse tree produced by IDLParser#statement_struct.
    def enterStatement_struct(self, ctx:IDLParser.Statement_structContext):
        pass

    # Exit a parse tree produced by IDLParser#statement_struct.
    def exitStatement_struct(self, ctx:IDLParser.Statement_structContext):
        pass


    # Enter a parse tree produced by IDLParser#statement_union.
    def enterStatement_union(self, ctx:IDLParser.Statement_unionContext):
        pass

    # Exit a parse tree produced by IDLParser#statement_union.
    def exitStatement_union(self, ctx:IDLParser.Statement_unionContext):
        pass


    # Enter a parse tree produced by IDLParser#statement_package.
    def enterStatement_package(self, ctx:IDLParser.Statement_packageContext):
        pass

    # Exit a parse tree produced by IDLParser#statement_package.
    def exitStatement_package(self, ctx:IDLParser.Statement_packageContext):
        pass


    # Enter a parse tree produced by IDLParser#statement_import.
    def enterStatement_import(self, ctx:IDLParser.Statement_importContext):
        pass

    # Exit a parse tree produced by IDLParser#statement_import.
    def exitStatement_import(self, ctx:IDLParser.Statement_importContext):
        pass


    # Enter a parse tree produced by IDLParser#statement_typedef.
    def enterStatement_typedef(self, ctx:IDLParser.Statement_typedefContext):
        pass

    # Exit a parse tree produced by IDLParser#statement_typedef.
    def exitStatement_typedef(self, ctx:IDLParser.Statement_typedefContext):
        pass


    # Enter a parse tree produced by IDLParser#statement_const.
    def enterStatement_const(self, ctx:IDLParser.Statement_constContext):
        pass

    # Exit a parse tree produced by IDLParser#statement_const.
    def exitStatement_const(self, ctx:IDLParser.Statement_constContext):
        pass


    # Enter a parse tree produced by IDLParser#const_type.
    def enterConst_type(self, ctx:IDLParser.Const_typeContext):
        pass

    # Exit a parse tree produced by IDLParser#const_type.
    def exitConst_type(self, ctx:IDLParser.Const_typeContext):
        pass


    # Enter a parse tree produced by IDLParser#method_block.
    def enterMethod_block(self, ctx:IDLParser.Method_blockContext):
        pass

    # Exit a parse tree produced by IDLParser#method_block.
    def exitMethod_block(self, ctx:IDLParser.Method_blockContext):
        pass


    # Enter a parse tree produced by IDLParser#method.
    def enterMethod(self, ctx:IDLParser.MethodContext):
        pass

    # Exit a parse tree produced by IDLParser#method.
    def exitMethod(self, ctx:IDLParser.MethodContext):
        pass


    # Enter a parse tree produced by IDLParser#method_arguments.
    def enterMethod_arguments(self, ctx:IDLParser.Method_argumentsContext):
        pass

    # Exit a parse tree produced by IDLParser#method_arguments.
    def exitMethod_arguments(self, ctx:IDLParser.Method_argumentsContext):
        pass


    # Enter a parse tree produced by IDLParser#method_argument.
    def enterMethod_argument(self, ctx:IDLParser.Method_argumentContext):
        pass

    # Exit a parse tree produced by IDLParser#method_argument.
    def exitMethod_argument(self, ctx:IDLParser.Method_argumentContext):
        pass


    # Enter a parse tree produced by IDLParser#declaration_block.
    def enterDeclaration_block(self, ctx:IDLParser.Declaration_blockContext):
        pass

    # Exit a parse tree produced by IDLParser#declaration_block.
    def exitDeclaration_block(self, ctx:IDLParser.Declaration_blockContext):
        pass


    # Enter a parse tree produced by IDLParser#declaration.
    def enterDeclaration(self, ctx:IDLParser.DeclarationContext):
        pass

    # Exit a parse tree produced by IDLParser#declaration.
    def exitDeclaration(self, ctx:IDLParser.DeclarationContext):
        pass


    # Enter a parse tree produced by IDLParser#type.
    def enterType(self, ctx:IDLParser.TypeContext):
        pass

    # Exit a parse tree produced by IDLParser#type.
    def exitType(self, ctx:IDLParser.TypeContext):
        pass


    # Enter a parse tree produced by IDLParser#type_arr.
    def enterType_arr(self, ctx:IDLParser.Type_arrContext):
        pass

    # Exit a parse tree produced by IDLParser#type_arr.
    def exitType_arr(self, ctx:IDLParser.Type_arrContext):
        pass


    # Enter a parse tree produced by IDLParser#type_arr_generic.
    def enterType_arr_generic(self, ctx:IDLParser.Type_arr_genericContext):
        pass

    # Exit a parse tree produced by IDLParser#type_arr_generic.
    def exitType_arr_generic(self, ctx:IDLParser.Type_arr_genericContext):
        pass



del IDLParser