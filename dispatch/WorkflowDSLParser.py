# Generated from WorkflowDSL.g4 by ANTLR 4.13.2
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
        4,1,18,72,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,0,1,
        0,1,0,1,0,5,0,17,8,0,10,0,12,0,20,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,
        1,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,5,3,38,8,3,10,3,12,3,41,9,
        3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,
        4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,65,8,4,1,5,1,5,1,5,1,5,1,5,1,5,0,0,
        6,0,2,4,6,8,10,0,0,76,0,18,1,0,0,0,2,23,1,0,0,0,4,28,1,0,0,0,6,33,
        1,0,0,0,8,64,1,0,0,0,10,66,1,0,0,0,12,17,3,2,1,0,13,17,3,4,2,0,14,
        17,3,6,3,0,15,17,3,10,5,0,16,12,1,0,0,0,16,13,1,0,0,0,16,14,1,0,
        0,0,16,15,1,0,0,0,17,20,1,0,0,0,18,16,1,0,0,0,18,19,1,0,0,0,19,21,
        1,0,0,0,20,18,1,0,0,0,21,22,5,0,0,1,22,1,1,0,0,0,23,24,5,1,0,0,24,
        25,5,16,0,0,25,26,5,2,0,0,26,27,5,16,0,0,27,3,1,0,0,0,28,29,5,3,
        0,0,29,30,5,16,0,0,30,31,5,2,0,0,31,32,5,16,0,0,32,5,1,0,0,0,33,
        34,5,4,0,0,34,35,5,16,0,0,35,39,5,5,0,0,36,38,3,8,4,0,37,36,1,0,
        0,0,38,41,1,0,0,0,39,37,1,0,0,0,39,40,1,0,0,0,40,42,1,0,0,0,41,39,
        1,0,0,0,42,43,5,6,0,0,43,7,1,0,0,0,44,45,5,7,0,0,45,65,5,16,0,0,
        46,47,5,8,0,0,47,65,5,16,0,0,48,49,5,9,0,0,49,65,5,16,0,0,50,51,
        5,10,0,0,51,65,5,16,0,0,52,53,5,11,0,0,53,54,5,16,0,0,54,55,5,12,
        0,0,55,65,3,8,4,0,56,57,5,13,0,0,57,58,5,14,0,0,58,59,5,16,0,0,59,
        60,5,12,0,0,60,65,3,8,4,0,61,62,5,15,0,0,62,63,5,12,0,0,63,65,3,
        8,4,0,64,44,1,0,0,0,64,46,1,0,0,0,64,48,1,0,0,0,64,50,1,0,0,0,64,
        52,1,0,0,0,64,56,1,0,0,0,64,61,1,0,0,0,65,9,1,0,0,0,66,67,5,7,0,
        0,67,68,5,16,0,0,68,69,5,2,0,0,69,70,5,16,0,0,70,11,1,0,0,0,4,16,
        18,39,64
    ]

class WorkflowDSLParser ( Parser ):

    grammarFileName = "WorkflowDSL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'@action'", "'='", "'@condition'", "'workflow'", 
                     "'{'", "'}'", "'action'", "'send'", "'recv'", "'goto'", 
                     "'if'", "':'", "'while'", "'not'", "'final'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "IDENT", "COMMENT", "WS" ]

    RULE_program = 0
    RULE_stepAlias = 1
    RULE_conditionAlias = 2
    RULE_workflowDef = 3
    RULE_statement = 4
    RULE_actionBinding = 5

    ruleNames =  [ "program", "stepAlias", "conditionAlias", "workflowDef", 
                   "statement", "actionBinding" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    IDENT=16
    COMMENT=17
    WS=18

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(WorkflowDSLParser.EOF, 0)

        def stepAlias(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(WorkflowDSLParser.StepAliasContext)
            else:
                return self.getTypedRuleContext(WorkflowDSLParser.StepAliasContext,i)


        def conditionAlias(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(WorkflowDSLParser.ConditionAliasContext)
            else:
                return self.getTypedRuleContext(WorkflowDSLParser.ConditionAliasContext,i)


        def workflowDef(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(WorkflowDSLParser.WorkflowDefContext)
            else:
                return self.getTypedRuleContext(WorkflowDSLParser.WorkflowDefContext,i)


        def actionBinding(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(WorkflowDSLParser.ActionBindingContext)
            else:
                return self.getTypedRuleContext(WorkflowDSLParser.ActionBindingContext,i)


        def getRuleIndex(self):
            return WorkflowDSLParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = WorkflowDSLParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 154) != 0):
                self.state = 16
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [1]:
                    self.state = 12
                    self.stepAlias()
                    pass
                elif token in [3]:
                    self.state = 13
                    self.conditionAlias()
                    pass
                elif token in [4]:
                    self.state = 14
                    self.workflowDef()
                    pass
                elif token in [7]:
                    self.state = 15
                    self.actionBinding()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 20
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 21
            self.match(WorkflowDSLParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StepAliasContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self, i:int=None):
            if i is None:
                return self.getTokens(WorkflowDSLParser.IDENT)
            else:
                return self.getToken(WorkflowDSLParser.IDENT, i)

        def getRuleIndex(self):
            return WorkflowDSLParser.RULE_stepAlias

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStepAlias" ):
                return visitor.visitStepAlias(self)
            else:
                return visitor.visitChildren(self)




    def stepAlias(self):

        localctx = WorkflowDSLParser.StepAliasContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stepAlias)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self.match(WorkflowDSLParser.T__0)
            self.state = 24
            self.match(WorkflowDSLParser.IDENT)
            self.state = 25
            self.match(WorkflowDSLParser.T__1)
            self.state = 26
            self.match(WorkflowDSLParser.IDENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionAliasContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self, i:int=None):
            if i is None:
                return self.getTokens(WorkflowDSLParser.IDENT)
            else:
                return self.getToken(WorkflowDSLParser.IDENT, i)

        def getRuleIndex(self):
            return WorkflowDSLParser.RULE_conditionAlias

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConditionAlias" ):
                return visitor.visitConditionAlias(self)
            else:
                return visitor.visitChildren(self)




    def conditionAlias(self):

        localctx = WorkflowDSLParser.ConditionAliasContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_conditionAlias)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self.match(WorkflowDSLParser.T__2)
            self.state = 29
            self.match(WorkflowDSLParser.IDENT)
            self.state = 30
            self.match(WorkflowDSLParser.T__1)
            self.state = 31
            self.match(WorkflowDSLParser.IDENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WorkflowDefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self):
            return self.getToken(WorkflowDSLParser.IDENT, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(WorkflowDSLParser.StatementContext)
            else:
                return self.getTypedRuleContext(WorkflowDSLParser.StatementContext,i)


        def getRuleIndex(self):
            return WorkflowDSLParser.RULE_workflowDef

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWorkflowDef" ):
                return visitor.visitWorkflowDef(self)
            else:
                return visitor.visitChildren(self)




    def workflowDef(self):

        localctx = WorkflowDSLParser.WorkflowDefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_workflowDef)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            self.match(WorkflowDSLParser.T__3)
            self.state = 34
            self.match(WorkflowDSLParser.IDENT)
            self.state = 35
            self.match(WorkflowDSLParser.T__4)
            self.state = 39
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 44928) != 0):
                self.state = 36
                self.statement()
                self.state = 41
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 42
            self.match(WorkflowDSLParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return WorkflowDSLParser.RULE_statement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class WhileBlockContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WorkflowDSLParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDENT(self):
            return self.getToken(WorkflowDSLParser.IDENT, 0)
        def statement(self):
            return self.getTypedRuleContext(WorkflowDSLParser.StatementContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileBlock" ):
                return visitor.visitWhileBlock(self)
            else:
                return visitor.visitChildren(self)


    class FinalBlockContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WorkflowDSLParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def statement(self):
            return self.getTypedRuleContext(WorkflowDSLParser.StatementContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFinalBlock" ):
                return visitor.visitFinalBlock(self)
            else:
                return visitor.visitChildren(self)


    class SendStmtContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WorkflowDSLParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDENT(self):
            return self.getToken(WorkflowDSLParser.IDENT, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSendStmt" ):
                return visitor.visitSendStmt(self)
            else:
                return visitor.visitChildren(self)


    class RecvStmtContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WorkflowDSLParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDENT(self):
            return self.getToken(WorkflowDSLParser.IDENT, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRecvStmt" ):
                return visitor.visitRecvStmt(self)
            else:
                return visitor.visitChildren(self)


    class GotoStmtContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WorkflowDSLParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDENT(self):
            return self.getToken(WorkflowDSLParser.IDENT, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGotoStmt" ):
                return visitor.visitGotoStmt(self)
            else:
                return visitor.visitChildren(self)


    class IfBlockContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WorkflowDSLParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDENT(self):
            return self.getToken(WorkflowDSLParser.IDENT, 0)
        def statement(self):
            return self.getTypedRuleContext(WorkflowDSLParser.StatementContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfBlock" ):
                return visitor.visitIfBlock(self)
            else:
                return visitor.visitChildren(self)


    class ActionStmtContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WorkflowDSLParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDENT(self):
            return self.getToken(WorkflowDSLParser.IDENT, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitActionStmt" ):
                return visitor.visitActionStmt(self)
            else:
                return visitor.visitChildren(self)



    def statement(self):

        localctx = WorkflowDSLParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_statement)
        try:
            self.state = 64
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                localctx = WorkflowDSLParser.ActionStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 44
                self.match(WorkflowDSLParser.T__6)
                self.state = 45
                self.match(WorkflowDSLParser.IDENT)
                pass
            elif token in [8]:
                localctx = WorkflowDSLParser.SendStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 46
                self.match(WorkflowDSLParser.T__7)
                self.state = 47
                self.match(WorkflowDSLParser.IDENT)
                pass
            elif token in [9]:
                localctx = WorkflowDSLParser.RecvStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 48
                self.match(WorkflowDSLParser.T__8)
                self.state = 49
                self.match(WorkflowDSLParser.IDENT)
                pass
            elif token in [10]:
                localctx = WorkflowDSLParser.GotoStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 50
                self.match(WorkflowDSLParser.T__9)
                self.state = 51
                self.match(WorkflowDSLParser.IDENT)
                pass
            elif token in [11]:
                localctx = WorkflowDSLParser.IfBlockContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 52
                self.match(WorkflowDSLParser.T__10)
                self.state = 53
                self.match(WorkflowDSLParser.IDENT)
                self.state = 54
                self.match(WorkflowDSLParser.T__11)
                self.state = 55
                self.statement()
                pass
            elif token in [13]:
                localctx = WorkflowDSLParser.WhileBlockContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 56
                self.match(WorkflowDSLParser.T__12)
                self.state = 57
                self.match(WorkflowDSLParser.T__13)
                self.state = 58
                self.match(WorkflowDSLParser.IDENT)
                self.state = 59
                self.match(WorkflowDSLParser.T__11)
                self.state = 60
                self.statement()
                pass
            elif token in [15]:
                localctx = WorkflowDSLParser.FinalBlockContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 61
                self.match(WorkflowDSLParser.T__14)
                self.state = 62
                self.match(WorkflowDSLParser.T__11)
                self.state = 63
                self.statement()
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


    class ActionBindingContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self, i:int=None):
            if i is None:
                return self.getTokens(WorkflowDSLParser.IDENT)
            else:
                return self.getToken(WorkflowDSLParser.IDENT, i)

        def getRuleIndex(self):
            return WorkflowDSLParser.RULE_actionBinding

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitActionBinding" ):
                return visitor.visitActionBinding(self)
            else:
                return visitor.visitChildren(self)




    def actionBinding(self):

        localctx = WorkflowDSLParser.ActionBindingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_actionBinding)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.match(WorkflowDSLParser.T__6)
            self.state = 67
            self.match(WorkflowDSLParser.IDENT)
            self.state = 68
            self.match(WorkflowDSLParser.T__1)
            self.state = 69
            self.match(WorkflowDSLParser.IDENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





