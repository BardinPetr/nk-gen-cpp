# Generated from /home/petr/Desktop/nk-cpp/grammar/IDL.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .IDLParser import IDLParser
else:
    from IDLParser import IDLParser

# This class defines a complete generic visitor for a parse tree produced by IDLParser.

class IDLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by IDLParser#idl.
    def visitIdl(self, ctx:IDLParser.IdlContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#interface.
    def visitInterface(self, ctx:IDLParser.InterfaceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#statements.
    def visitStatements(self, ctx:IDLParser.StatementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#statement.
    def visitStatement(self, ctx:IDLParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#statement_struct.
    def visitStatement_struct(self, ctx:IDLParser.Statement_structContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#statement_union.
    def visitStatement_union(self, ctx:IDLParser.Statement_unionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#statement_package.
    def visitStatement_package(self, ctx:IDLParser.Statement_packageContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#statement_import.
    def visitStatement_import(self, ctx:IDLParser.Statement_importContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#statement_typedef.
    def visitStatement_typedef(self, ctx:IDLParser.Statement_typedefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#statement_const.
    def visitStatement_const(self, ctx:IDLParser.Statement_constContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#const_type.
    def visitConst_type(self, ctx:IDLParser.Const_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#method_block.
    def visitMethod_block(self, ctx:IDLParser.Method_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#method.
    def visitMethod(self, ctx:IDLParser.MethodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#method_arguments.
    def visitMethod_arguments(self, ctx:IDLParser.Method_argumentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#method_argument.
    def visitMethod_argument(self, ctx:IDLParser.Method_argumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#declaration_block.
    def visitDeclaration_block(self, ctx:IDLParser.Declaration_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#declaration.
    def visitDeclaration(self, ctx:IDLParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#type.
    def visitType(self, ctx:IDLParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#type_arr.
    def visitType_arr(self, ctx:IDLParser.Type_arrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#type_arr_generic.
    def visitType_arr_generic(self, ctx:IDLParser.Type_arr_genericContext):
        return self.visitChildren(ctx)



del IDLParser