# Generated from /home/petr/Desktop/nk-cpp/grammar/IDL.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys

if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4, 1, 34, 151, 2, 0, 7, 0, 2, 1, 7, 1, 2, 2, 7, 2, 2, 3, 7, 3, 2, 4, 7, 4, 2, 5, 7, 5, 2, 6, 7,
        6, 2, 7, 7, 7, 2, 8, 7, 8, 2, 9, 7, 9, 2, 10, 7, 10, 2, 11, 7, 11, 2, 12, 7, 12, 2, 13, 7, 13,
        2, 14, 7, 14, 2, 15, 7, 15, 2, 16, 7, 16, 2, 17, 7, 17, 2, 18, 7, 18, 2, 19, 7, 19, 1, 0,
        1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 5, 2, 52, 8, 2, 10, 2, 12, 2, 55,
        9, 2, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 3, 3, 62, 8, 3, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 5, 1,
        5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 6, 1, 6, 1, 6, 1, 7, 1, 7, 1, 7, 1, 8, 1, 8, 1, 8, 1, 8, 1, 8, 1,
        9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 10, 1, 10, 1, 11, 1, 11, 1, 11, 5, 11, 99, 8, 11,
        10, 11, 12, 11, 102, 9, 11, 1, 12, 1, 12, 1, 12, 3, 12, 107, 8, 12, 1, 12, 1, 12, 1, 13,
        1, 13, 1, 13, 5, 13, 114, 8, 13, 10, 13, 12, 13, 117, 9, 13, 1, 14, 1, 14, 1, 14, 1, 15,
        1, 15, 1, 15, 5, 15, 125, 8, 15, 10, 15, 12, 15, 128, 9, 15, 1, 16, 1, 16, 1, 16, 1, 17,
        1, 17, 1, 17, 1, 17, 3, 17, 137, 8, 17, 1, 18, 1, 18, 1, 18, 1, 18, 1, 18, 1, 19, 1, 19,
        1, 19, 1, 19, 1, 19, 1, 19, 1, 19, 1, 19, 0, 0, 20, 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20,
        22, 24, 26, 28, 30, 32, 34, 36, 38, 0, 2, 2, 0, 17, 17, 30, 30, 2, 0, 28, 28, 30, 30, 142,
        0, 40, 1, 0, 0, 0, 2, 45, 1, 0, 0, 0, 4, 53, 1, 0, 0, 0, 6, 61, 1, 0, 0, 0, 8, 63, 1, 0, 0, 0,
        10, 69, 1, 0, 0, 0, 12, 75, 1, 0, 0, 0, 14, 78, 1, 0, 0, 0, 16, 81, 1, 0, 0, 0, 18, 86, 1,
        0, 0, 0, 20, 93, 1, 0, 0, 0, 22, 100, 1, 0, 0, 0, 24, 103, 1, 0, 0, 0, 26, 110, 1, 0, 0, 0,
        28, 118, 1, 0, 0, 0, 30, 126, 1, 0, 0, 0, 32, 129, 1, 0, 0, 0, 34, 136, 1, 0, 0, 0, 36, 138,
        1, 0, 0, 0, 38, 143, 1, 0, 0, 0, 40, 41, 3, 12, 6, 0, 41, 42, 3, 4, 2, 0, 42, 43, 3, 2, 1,
        0, 43, 44, 5, 0, 0, 1, 44, 1, 1, 0, 0, 0, 45, 46, 5, 1, 0, 0, 46, 47, 5, 2, 0, 0, 47, 48, 3,
        22, 11, 0, 48, 49, 5, 3, 0, 0, 49, 3, 1, 0, 0, 0, 50, 52, 3, 6, 3, 0, 51, 50, 1, 0, 0, 0, 52,
        55, 1, 0, 0, 0, 53, 51, 1, 0, 0, 0, 53, 54, 1, 0, 0, 0, 54, 5, 1, 0, 0, 0, 55, 53, 1, 0, 0,
        0, 56, 62, 3, 18, 9, 0, 57, 62, 3, 16, 8, 0, 58, 62, 3, 14, 7, 0, 59, 62, 3, 8, 4, 0, 60,
        62, 3, 10, 5, 0, 61, 56, 1, 0, 0, 0, 61, 57, 1, 0, 0, 0, 61, 58, 1, 0, 0, 0, 61, 59, 1, 0,
        0, 0, 61, 60, 1, 0, 0, 0, 62, 7, 1, 0, 0, 0, 63, 64, 5, 4, 0, 0, 64, 65, 5, 30, 0, 0, 65, 66,
        5, 2, 0, 0, 66, 67, 3, 30, 15, 0, 67, 68, 5, 3, 0, 0, 68, 9, 1, 0, 0, 0, 69, 70, 5, 5, 0, 0,
        70, 71, 5, 30, 0, 0, 71, 72, 5, 2, 0, 0, 72, 73, 3, 30, 15, 0, 73, 74, 5, 3, 0, 0, 74, 11,
        1, 0, 0, 0, 75, 76, 5, 6, 0, 0, 76, 77, 5, 31, 0, 0, 77, 13, 1, 0, 0, 0, 78, 79, 5, 7, 0, 0,
        79, 80, 5, 31, 0, 0, 80, 15, 1, 0, 0, 0, 81, 82, 5, 8, 0, 0, 82, 83, 3, 34, 17, 0, 83, 84,
        5, 30, 0, 0, 84, 85, 5, 9, 0, 0, 85, 17, 1, 0, 0, 0, 86, 87, 5, 10, 0, 0, 87, 88, 3, 20, 10,
        0, 88, 89, 5, 30, 0, 0, 89, 90, 5, 11, 0, 0, 90, 91, 5, 28, 0, 0, 91, 92, 5, 9, 0, 0, 92,
        19, 1, 0, 0, 0, 93, 94, 7, 0, 0, 0, 94, 21, 1, 0, 0, 0, 95, 96, 3, 24, 12, 0, 96, 97, 5, 9,
        0, 0, 97, 99, 1, 0, 0, 0, 98, 95, 1, 0, 0, 0, 99, 102, 1, 0, 0, 0, 100, 98, 1, 0, 0, 0, 100,
        101, 1, 0, 0, 0, 101, 23, 1, 0, 0, 0, 102, 100, 1, 0, 0, 0, 103, 104, 5, 30, 0, 0, 104,
        106, 5, 12, 0, 0, 105, 107, 3, 26, 13, 0, 106, 105, 1, 0, 0, 0, 106, 107, 1, 0, 0, 0, 107,
        108, 1, 0, 0, 0, 108, 109, 5, 13, 0, 0, 109, 25, 1, 0, 0, 0, 110, 115, 3, 28, 14, 0, 111,
        112, 5, 14, 0, 0, 112, 114, 3, 28, 14, 0, 113, 111, 1, 0, 0, 0, 114, 117, 1, 0, 0, 0, 115,
        113, 1, 0, 0, 0, 115, 116, 1, 0, 0, 0, 116, 27, 1, 0, 0, 0, 117, 115, 1, 0, 0, 0, 118, 119,
        5, 27, 0, 0, 119, 120, 3, 32, 16, 0, 120, 29, 1, 0, 0, 0, 121, 122, 3, 32, 16, 0, 122,
        123, 5, 9, 0, 0, 123, 125, 1, 0, 0, 0, 124, 121, 1, 0, 0, 0, 125, 128, 1, 0, 0, 0, 126,
        124, 1, 0, 0, 0, 126, 127, 1, 0, 0, 0, 127, 31, 1, 0, 0, 0, 128, 126, 1, 0, 0, 0, 129, 130,
        3, 34, 17, 0, 130, 131, 5, 30, 0, 0, 131, 33, 1, 0, 0, 0, 132, 137, 5, 30, 0, 0, 133, 137,
        5, 17, 0, 0, 134, 137, 3, 36, 18, 0, 135, 137, 3, 38, 19, 0, 136, 132, 1, 0, 0, 0, 136,
        133, 1, 0, 0, 0, 136, 134, 1, 0, 0, 0, 136, 135, 1, 0, 0, 0, 137, 35, 1, 0, 0, 0, 138, 139,
        5, 21, 0, 0, 139, 140, 5, 15, 0, 0, 140, 141, 7, 1, 0, 0, 141, 142, 5, 16, 0, 0, 142, 37,
        1, 0, 0, 0, 143, 144, 5, 24, 0, 0, 144, 145, 5, 15, 0, 0, 145, 146, 3, 34, 17, 0, 146,
        147, 5, 14, 0, 0, 147, 148, 7, 1, 0, 0, 148, 149, 5, 16, 0, 0, 149, 39, 1, 0, 0, 0, 7, 53,
        61, 100, 106, 115, 126, 136
    ]


class IDLParser(Parser):
    grammarFileName = "IDL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [DFA(ds, i) for i, ds in enumerate(atn.decisionToState)]

    sharedContextCache = PredictionContextCache()

    literalNames = ["<INVALID>", "'interface'", "'{'", "'}'", "'struct'",
                    "'union'", "'package'", "'import'", "'typedef'", "';'",
                    "'const'", "'='", "'('", "')'", "','", "'<'", "'>'",
                    "<INVALID>", "<INVALID>", "<INVALID>", "'Handle'",
                    "<INVALID>", "'bytes'", "'string'", "<INVALID>", "'array'",
                    "'sequence'"]

    symbolicNames = ["<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                     "<INVALID>", "TYPE_PRIMITIVE", "TYPE_SINT", "TYPE_UINT",
                     "TYPE_HANDLE", "TYPE_ARR", "TYPE_BYTES", "TYPE_STRING",
                     "TYPE_ARR_GENERIC", "TYPE_ARRAY", "TYPE_SEQUENCE",
                     "ARG_DIRECTION", "INT", "INT_HEX", "ID", "PACKAGE_ID",
                     "COMMENT", "OL_COMMENT", "SPACE"]

    RULE_idl = 0
    RULE_interface = 1
    RULE_statements = 2
    RULE_statement = 3
    RULE_statement_struct = 4
    RULE_statement_union = 5
    RULE_statement_package = 6
    RULE_statement_import = 7
    RULE_statement_typedef = 8
    RULE_statement_const = 9
    RULE_const_type = 10
    RULE_method_block = 11
    RULE_method = 12
    RULE_method_arguments = 13
    RULE_method_argument = 14
    RULE_declaration_block = 15
    RULE_declaration = 16
    RULE_type = 17
    RULE_type_arr = 18
    RULE_type_arr_generic = 19

    ruleNames = ["idl", "interface", "statements", "statement", "statement_struct",
                 "statement_union", "statement_package", "statement_import",
                 "statement_typedef", "statement_const", "const_type",
                 "method_block", "method", "method_arguments", "method_argument",
                 "declaration_block", "declaration", "type", "type_arr",
                 "type_arr_generic"]

    EOF = Token.EOF
    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    T__11 = 12
    T__12 = 13
    T__13 = 14
    T__14 = 15
    T__15 = 16
    TYPE_PRIMITIVE = 17
    TYPE_SINT = 18
    TYPE_UINT = 19
    TYPE_HANDLE = 20
    TYPE_ARR = 21
    TYPE_BYTES = 22
    TYPE_STRING = 23
    TYPE_ARR_GENERIC = 24
    TYPE_ARRAY = 25
    TYPE_SEQUENCE = 26
    ARG_DIRECTION = 27
    INT = 28
    INT_HEX = 29
    ID = 30
    PACKAGE_ID = 31
    COMMENT = 32
    OL_COMMENT = 33
    SPACE = 34

    def __init__(self, input: TokenStream, output: TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None

    class IdlContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement_package(self):
            return self.getTypedRuleContext(IDLParser.Statement_packageContext, 0)

        def statements(self):
            return self.getTypedRuleContext(IDLParser.StatementsContext, 0)

        def interface(self):
            return self.getTypedRuleContext(IDLParser.InterfaceContext, 0)

        def EOF(self):
            return self.getToken(IDLParser.EOF, 0)

        def getRuleIndex(self):
            return IDLParser.RULE_idl

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterIdl"):
                listener.enterIdl(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitIdl"):
                listener.exitIdl(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitIdl"):
                return visitor.visitIdl(self)
            else:
                return visitor.visitChildren(self)

    def idl(self):

        localctx = IDLParser.IdlContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_idl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.statement_package()
            self.state = 41
            self.statements()
            self.state = 42
            self.interface()
            self.state = 43
            self.match(IDLParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class InterfaceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def method_block(self):
            return self.getTypedRuleContext(IDLParser.Method_blockContext, 0)

        def getRuleIndex(self):
            return IDLParser.RULE_interface

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterInterface"):
                listener.enterInterface(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitInterface"):
                listener.exitInterface(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitInterface"):
                return visitor.visitInterface(self)
            else:
                return visitor.visitChildren(self)

    def interface(self):

        localctx = IDLParser.InterfaceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_interface)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self.match(IDLParser.T__0)
            self.state = 46
            self.match(IDLParser.T__1)
            self.state = 47
            self.method_block()
            self.state = 48
            self.match(IDLParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StatementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(IDLParser.StatementContext)
            else:
                return self.getTypedRuleContext(IDLParser.StatementContext, i)

        def getRuleIndex(self):
            return IDLParser.RULE_statements

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterStatements"):
                listener.enterStatements(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitStatements"):
                listener.exitStatements(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitStatements"):
                return visitor.visitStatements(self)
            else:
                return visitor.visitChildren(self)

    def statements(self):

        localctx = IDLParser.StatementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statements)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1456) != 0):
                self.state = 50
                self.statement()
                self.state = 55
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement_const(self):
            return self.getTypedRuleContext(IDLParser.Statement_constContext, 0)

        def statement_typedef(self):
            return self.getTypedRuleContext(IDLParser.Statement_typedefContext, 0)

        def statement_import(self):
            return self.getTypedRuleContext(IDLParser.Statement_importContext, 0)

        def statement_struct(self):
            return self.getTypedRuleContext(IDLParser.Statement_structContext, 0)

        def statement_union(self):
            return self.getTypedRuleContext(IDLParser.Statement_unionContext, 0)

        def getRuleIndex(self):
            return IDLParser.RULE_statement

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterStatement"):
                listener.enterStatement(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitStatement"):
                listener.exitStatement(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitStatement"):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)

    def statement(self):

        localctx = IDLParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_statement)
        try:
            self.state = 61
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                self.enterOuterAlt(localctx, 1)
                self.state = 56
                self.statement_const()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 2)
                self.state = 57
                self.statement_typedef()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 3)
                self.state = 58
                self.statement_import()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 4)
                self.state = 59
                self.statement_struct()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 5)
                self.state = 60
                self.statement_union()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Statement_structContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(IDLParser.ID, 0)

        def declaration_block(self):
            return self.getTypedRuleContext(IDLParser.Declaration_blockContext, 0)

        def getRuleIndex(self):
            return IDLParser.RULE_statement_struct

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterStatement_struct"):
                listener.enterStatement_struct(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitStatement_struct"):
                listener.exitStatement_struct(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitStatement_struct"):
                return visitor.visitStatement_struct(self)
            else:
                return visitor.visitChildren(self)

    def statement_struct(self):

        localctx = IDLParser.Statement_structContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_statement_struct)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self.match(IDLParser.T__3)
            self.state = 64
            self.match(IDLParser.ID)
            self.state = 65
            self.match(IDLParser.T__1)
            self.state = 66
            self.declaration_block()
            self.state = 67
            self.match(IDLParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Statement_unionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(IDLParser.ID, 0)

        def declaration_block(self):
            return self.getTypedRuleContext(IDLParser.Declaration_blockContext, 0)

        def getRuleIndex(self):
            return IDLParser.RULE_statement_union

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterStatement_union"):
                listener.enterStatement_union(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitStatement_union"):
                listener.exitStatement_union(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitStatement_union"):
                return visitor.visitStatement_union(self)
            else:
                return visitor.visitChildren(self)

    def statement_union(self):

        localctx = IDLParser.Statement_unionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_statement_union)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self.match(IDLParser.T__4)
            self.state = 70
            self.match(IDLParser.ID)
            self.state = 71
            self.match(IDLParser.T__1)
            self.state = 72
            self.declaration_block()
            self.state = 73
            self.match(IDLParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Statement_packageContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PACKAGE_ID(self):
            return self.getToken(IDLParser.PACKAGE_ID, 0)

        def getRuleIndex(self):
            return IDLParser.RULE_statement_package

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterStatement_package"):
                listener.enterStatement_package(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitStatement_package"):
                listener.exitStatement_package(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitStatement_package"):
                return visitor.visitStatement_package(self)
            else:
                return visitor.visitChildren(self)

    def statement_package(self):

        localctx = IDLParser.Statement_packageContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_statement_package)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self.match(IDLParser.T__5)
            self.state = 76
            self.match(IDLParser.PACKAGE_ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Statement_importContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PACKAGE_ID(self):
            return self.getToken(IDLParser.PACKAGE_ID, 0)

        def getRuleIndex(self):
            return IDLParser.RULE_statement_import

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterStatement_import"):
                listener.enterStatement_import(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitStatement_import"):
                listener.exitStatement_import(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitStatement_import"):
                return visitor.visitStatement_import(self)
            else:
                return visitor.visitChildren(self)

    def statement_import(self):

        localctx = IDLParser.Statement_importContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_statement_import)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self.match(IDLParser.T__6)
            self.state = 79
            self.match(IDLParser.PACKAGE_ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Statement_typedefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(IDLParser.TypeContext, 0)

        def ID(self):
            return self.getToken(IDLParser.ID, 0)

        def getRuleIndex(self):
            return IDLParser.RULE_statement_typedef

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterStatement_typedef"):
                listener.enterStatement_typedef(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitStatement_typedef"):
                listener.exitStatement_typedef(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitStatement_typedef"):
                return visitor.visitStatement_typedef(self)
            else:
                return visitor.visitChildren(self)

    def statement_typedef(self):

        localctx = IDLParser.Statement_typedefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_statement_typedef)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self.match(IDLParser.T__7)
            self.state = 82
            self.type_()
            self.state = 83
            self.match(IDLParser.ID)
            self.state = 84
            self.match(IDLParser.T__8)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Statement_constContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def const_type(self):
            return self.getTypedRuleContext(IDLParser.Const_typeContext, 0)

        def ID(self):
            return self.getToken(IDLParser.ID, 0)

        def INT(self):
            return self.getToken(IDLParser.INT, 0)

        def getRuleIndex(self):
            return IDLParser.RULE_statement_const

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterStatement_const"):
                listener.enterStatement_const(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitStatement_const"):
                listener.exitStatement_const(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitStatement_const"):
                return visitor.visitStatement_const(self)
            else:
                return visitor.visitChildren(self)

    def statement_const(self):

        localctx = IDLParser.Statement_constContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_statement_const)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.match(IDLParser.T__9)
            self.state = 87
            self.const_type()
            self.state = 88
            self.match(IDLParser.ID)
            self.state = 89
            self.match(IDLParser.T__10)
            self.state = 90
            self.match(IDLParser.INT)
            self.state = 91
            self.match(IDLParser.T__8)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Const_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE_PRIMITIVE(self):
            return self.getToken(IDLParser.TYPE_PRIMITIVE, 0)

        def ID(self):
            return self.getToken(IDLParser.ID, 0)

        def getRuleIndex(self):
            return IDLParser.RULE_const_type

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterConst_type"):
                listener.enterConst_type(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitConst_type"):
                listener.exitConst_type(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitConst_type"):
                return visitor.visitConst_type(self)
            else:
                return visitor.visitChildren(self)

    def const_type(self):

        localctx = IDLParser.Const_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_const_type)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            _la = self._input.LA(1)
            if not (_la == 17 or _la == 30):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Method_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def method(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(IDLParser.MethodContext)
            else:
                return self.getTypedRuleContext(IDLParser.MethodContext, i)

        def getRuleIndex(self):
            return IDLParser.RULE_method_block

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterMethod_block"):
                listener.enterMethod_block(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitMethod_block"):
                listener.exitMethod_block(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitMethod_block"):
                return visitor.visitMethod_block(self)
            else:
                return visitor.visitChildren(self)

    def method_block(self):

        localctx = IDLParser.Method_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_method_block)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la == 30:
                self.state = 95
                self.method()
                self.state = 96
                self.match(IDLParser.T__8)
                self.state = 102
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class MethodContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(IDLParser.ID, 0)

        def method_arguments(self):
            return self.getTypedRuleContext(IDLParser.Method_argumentsContext, 0)

        def getRuleIndex(self):
            return IDLParser.RULE_method

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterMethod"):
                listener.enterMethod(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitMethod"):
                listener.exitMethod(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitMethod"):
                return visitor.visitMethod(self)
            else:
                return visitor.visitChildren(self)

    def method(self):

        localctx = IDLParser.MethodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_method)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            self.match(IDLParser.ID)
            self.state = 104
            self.match(IDLParser.T__11)
            self.state = 106
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == 27:
                self.state = 105
                self.method_arguments()

            self.state = 108
            self.match(IDLParser.T__12)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Method_argumentsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def method_argument(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(IDLParser.Method_argumentContext)
            else:
                return self.getTypedRuleContext(IDLParser.Method_argumentContext, i)

        def getRuleIndex(self):
            return IDLParser.RULE_method_arguments

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterMethod_arguments"):
                listener.enterMethod_arguments(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitMethod_arguments"):
                listener.exitMethod_arguments(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitMethod_arguments"):
                return visitor.visitMethod_arguments(self)
            else:
                return visitor.visitChildren(self)

    def method_arguments(self):

        localctx = IDLParser.Method_argumentsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_method_arguments)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self.method_argument()
            self.state = 115
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la == 14:
                self.state = 111
                self.match(IDLParser.T__13)
                self.state = 112
                self.method_argument()
                self.state = 117
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Method_argumentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARG_DIRECTION(self):
            return self.getToken(IDLParser.ARG_DIRECTION, 0)

        def declaration(self):
            return self.getTypedRuleContext(IDLParser.DeclarationContext, 0)

        def getRuleIndex(self):
            return IDLParser.RULE_method_argument

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterMethod_argument"):
                listener.enterMethod_argument(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitMethod_argument"):
                listener.exitMethod_argument(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitMethod_argument"):
                return visitor.visitMethod_argument(self)
            else:
                return visitor.visitChildren(self)

    def method_argument(self):

        localctx = IDLParser.Method_argumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_method_argument)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            self.match(IDLParser.ARG_DIRECTION)
            self.state = 119
            self.declaration()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Declaration_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(IDLParser.DeclarationContext)
            else:
                return self.getTypedRuleContext(IDLParser.DeclarationContext, i)

        def getRuleIndex(self):
            return IDLParser.RULE_declaration_block

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterDeclaration_block"):
                listener.enterDeclaration_block(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitDeclaration_block"):
                listener.exitDeclaration_block(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitDeclaration_block"):
                return visitor.visitDeclaration_block(self)
            else:
                return visitor.visitChildren(self)

    def declaration_block(self):

        localctx = IDLParser.Declaration_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_declaration_block)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 126
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1092747264) != 0):
                self.state = 121
                self.declaration()
                self.state = 122
                self.match(IDLParser.T__8)
                self.state = 128
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(IDLParser.TypeContext, 0)

        def ID(self):
            return self.getToken(IDLParser.ID, 0)

        def getRuleIndex(self):
            return IDLParser.RULE_declaration

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterDeclaration"):
                listener.enterDeclaration(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitDeclaration"):
                listener.exitDeclaration(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitDeclaration"):
                return visitor.visitDeclaration(self)
            else:
                return visitor.visitChildren(self)

    def declaration(self):

        localctx = IDLParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
            self.type_()
            self.state = 130
            self.match(IDLParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(IDLParser.ID, 0)

        def TYPE_PRIMITIVE(self):
            return self.getToken(IDLParser.TYPE_PRIMITIVE, 0)

        def type_arr(self):
            return self.getTypedRuleContext(IDLParser.Type_arrContext, 0)

        def type_arr_generic(self):
            return self.getTypedRuleContext(IDLParser.Type_arr_genericContext, 0)

        def getRuleIndex(self):
            return IDLParser.RULE_type

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterType"):
                listener.enterType(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitType"):
                listener.exitType(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitType"):
                return visitor.visitType(self)
            else:
                return visitor.visitChildren(self)

    def type_(self):

        localctx = IDLParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_type)
        try:
            self.state = 136
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [30]:
                self.enterOuterAlt(localctx, 1)
                self.state = 132
                self.match(IDLParser.ID)
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 2)
                self.state = 133
                self.match(IDLParser.TYPE_PRIMITIVE)
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 3)
                self.state = 134
                self.type_arr()
                pass
            elif token in [24]:
                self.enterOuterAlt(localctx, 4)
                self.state = 135
                self.type_arr_generic()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Type_arrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE_ARR(self):
            return self.getToken(IDLParser.TYPE_ARR, 0)

        def INT(self):
            return self.getToken(IDLParser.INT, 0)

        def ID(self):
            return self.getToken(IDLParser.ID, 0)

        def getRuleIndex(self):
            return IDLParser.RULE_type_arr

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterType_arr"):
                listener.enterType_arr(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitType_arr"):
                listener.exitType_arr(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitType_arr"):
                return visitor.visitType_arr(self)
            else:
                return visitor.visitChildren(self)

    def type_arr(self):

        localctx = IDLParser.Type_arrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_type_arr)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 138
            self.match(IDLParser.TYPE_ARR)
            self.state = 139
            self.match(IDLParser.T__14)
            self.state = 140
            _la = self._input.LA(1)
            if not (_la == 28 or _la == 30):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 141
            self.match(IDLParser.T__15)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Type_arr_genericContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE_ARR_GENERIC(self):
            return self.getToken(IDLParser.TYPE_ARR_GENERIC, 0)

        def type_(self):
            return self.getTypedRuleContext(IDLParser.TypeContext, 0)

        def INT(self):
            return self.getToken(IDLParser.INT, 0)

        def ID(self):
            return self.getToken(IDLParser.ID, 0)

        def getRuleIndex(self):
            return IDLParser.RULE_type_arr_generic

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterType_arr_generic"):
                listener.enterType_arr_generic(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitType_arr_generic"):
                listener.exitType_arr_generic(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitType_arr_generic"):
                return visitor.visitType_arr_generic(self)
            else:
                return visitor.visitChildren(self)

    def type_arr_generic(self):

        localctx = IDLParser.Type_arr_genericContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_type_arr_generic)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 143
            self.match(IDLParser.TYPE_ARR_GENERIC)
            self.state = 144
            self.match(IDLParser.T__14)
            self.state = 145
            self.type_()
            self.state = 146
            self.match(IDLParser.T__13)
            self.state = 147
            _la = self._input.LA(1)
            if not (_la == 28 or _la == 30):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 148
            self.match(IDLParser.T__15)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx
