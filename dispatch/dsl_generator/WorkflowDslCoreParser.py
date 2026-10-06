# Generated from WorkflowDslCore.g4 by ANTLR 4.13.2
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
        4,1,10,66,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,1,0,1,0,5,0,21,8,0,10,0,12,0,24,9,0,1,0,1,0,1,
        1,3,1,29,8,1,1,1,1,1,1,1,1,2,3,2,35,8,2,1,2,1,2,1,2,1,3,1,3,1,3,
        1,3,1,3,1,3,3,3,46,8,3,1,4,5,4,49,8,4,10,4,12,4,52,9,4,1,5,1,5,1,
        6,3,6,57,8,6,1,6,1,6,1,6,1,7,1,7,1,8,1,8,1,8,0,0,9,0,2,4,6,8,10,
        12,14,16,0,0,63,0,22,1,0,0,0,2,28,1,0,0,0,4,34,1,0,0,0,6,39,1,0,
        0,0,8,50,1,0,0,0,10,53,1,0,0,0,12,56,1,0,0,0,14,61,1,0,0,0,16,63,
        1,0,0,0,18,21,3,2,1,0,19,21,3,4,2,0,20,18,1,0,0,0,20,19,1,0,0,0,
        21,24,1,0,0,0,22,20,1,0,0,0,22,23,1,0,0,0,23,25,1,0,0,0,24,22,1,
        0,0,0,25,26,5,0,0,1,26,1,1,0,0,0,27,29,5,7,0,0,28,27,1,0,0,0,28,
        29,1,0,0,0,29,30,1,0,0,0,30,31,5,1,0,0,31,32,3,6,3,0,32,3,1,0,0,
        0,33,35,5,7,0,0,34,33,1,0,0,0,34,35,1,0,0,0,35,36,1,0,0,0,36,37,
        5,2,0,0,37,38,3,6,3,0,38,5,1,0,0,0,39,40,3,16,8,0,40,41,5,3,0,0,
        41,42,5,7,0,0,42,43,3,8,4,0,43,45,5,4,0,0,44,46,5,7,0,0,45,44,1,
        0,0,0,45,46,1,0,0,0,46,7,1,0,0,0,47,49,3,10,5,0,48,47,1,0,0,0,49,
        52,1,0,0,0,50,48,1,0,0,0,50,51,1,0,0,0,51,9,1,0,0,0,52,50,1,0,0,
        0,53,54,3,12,6,0,54,11,1,0,0,0,55,57,5,5,0,0,56,55,1,0,0,0,56,57,
        1,0,0,0,57,58,1,0,0,0,58,59,3,14,7,0,59,60,5,7,0,0,60,13,1,0,0,0,
        61,62,5,6,0,0,62,15,1,0,0,0,63,64,5,6,0,0,64,17,1,0,0,0,7,20,22,
        28,34,45,50,56
    ]

class WorkflowDslCoreParser ( Parser ):

    grammarFileName = "WorkflowDslCore.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'workflow'", "'procedure'", "'{'", "'}'", 
                     "'ignore'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "Ignore", "ID", "NEWLINE", "SPACE", "COMMENT", 
                      "LINE_COMMENT" ]

    RULE_workflowFile = 0
    RULE_workflow = 1
    RULE_procedure = 2
    RULE_procedureBody = 3
    RULE_sequenceAction = 4
    RULE_action = 5
    RULE_syncAction = 6
    RULE_function = 7
    RULE_identifier = 8

    ruleNames =  [ "workflowFile", "workflow", "procedure", "procedureBody", 
                   "sequenceAction", "action", "syncAction", "function", 
                   "identifier" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    Ignore=5
    ID=6
    NEWLINE=7
    SPACE=8
    COMMENT=9
    LINE_COMMENT=10

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class WorkflowFileContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(WorkflowDslCoreParser.EOF, 0)

        def workflow(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(WorkflowDslCoreParser.WorkflowContext)
            else:
                return self.getTypedRuleContext(WorkflowDslCoreParser.WorkflowContext,i)


        def procedure(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(WorkflowDslCoreParser.ProcedureContext)
            else:
                return self.getTypedRuleContext(WorkflowDslCoreParser.ProcedureContext,i)


        def getRuleIndex(self):
            return WorkflowDslCoreParser.RULE_workflowFile

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWorkflowFile" ):
                return visitor.visitWorkflowFile(self)
            else:
                return visitor.visitChildren(self)




    def workflowFile(self):

        localctx = WorkflowDslCoreParser.WorkflowFileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_workflowFile)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 134) != 0):
                self.state = 20
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 18
                    self.workflow()
                    pass

                elif la_ == 2:
                    self.state = 19
                    self.procedure()
                    pass


                self.state = 24
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 25
            self.match(WorkflowDslCoreParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WorkflowContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def procedureBody(self):
            return self.getTypedRuleContext(WorkflowDslCoreParser.ProcedureBodyContext,0)


        def NEWLINE(self):
            return self.getToken(WorkflowDslCoreParser.NEWLINE, 0)

        def getRuleIndex(self):
            return WorkflowDslCoreParser.RULE_workflow

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWorkflow" ):
                return visitor.visitWorkflow(self)
            else:
                return visitor.visitChildren(self)




    def workflow(self):

        localctx = WorkflowDslCoreParser.WorkflowContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_workflow)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 27
                self.match(WorkflowDslCoreParser.NEWLINE)


            self.state = 30
            self.match(WorkflowDslCoreParser.T__0)
            self.state = 31
            self.procedureBody()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProcedureContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def procedureBody(self):
            return self.getTypedRuleContext(WorkflowDslCoreParser.ProcedureBodyContext,0)


        def NEWLINE(self):
            return self.getToken(WorkflowDslCoreParser.NEWLINE, 0)

        def getRuleIndex(self):
            return WorkflowDslCoreParser.RULE_procedure

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProcedure" ):
                return visitor.visitProcedure(self)
            else:
                return visitor.visitChildren(self)




    def procedure(self):

        localctx = WorkflowDslCoreParser.ProcedureContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_procedure)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 33
                self.match(WorkflowDslCoreParser.NEWLINE)


            self.state = 36
            self.match(WorkflowDslCoreParser.T__1)
            self.state = 37
            self.procedureBody()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProcedureBodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(WorkflowDslCoreParser.IdentifierContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(WorkflowDslCoreParser.NEWLINE)
            else:
                return self.getToken(WorkflowDslCoreParser.NEWLINE, i)

        def sequenceAction(self):
            return self.getTypedRuleContext(WorkflowDslCoreParser.SequenceActionContext,0)


        def getRuleIndex(self):
            return WorkflowDslCoreParser.RULE_procedureBody

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProcedureBody" ):
                return visitor.visitProcedureBody(self)
            else:
                return visitor.visitChildren(self)




    def procedureBody(self):

        localctx = WorkflowDslCoreParser.ProcedureBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_procedureBody)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self.identifier()
            self.state = 40
            self.match(WorkflowDslCoreParser.T__2)
            self.state = 41
            self.match(WorkflowDslCoreParser.NEWLINE)
            self.state = 42
            self.sequenceAction()
            self.state = 43
            self.match(WorkflowDslCoreParser.T__3)
            self.state = 45
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 44
                self.match(WorkflowDslCoreParser.NEWLINE)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SequenceActionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def action(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(WorkflowDslCoreParser.ActionContext)
            else:
                return self.getTypedRuleContext(WorkflowDslCoreParser.ActionContext,i)


        def getRuleIndex(self):
            return WorkflowDslCoreParser.RULE_sequenceAction

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSequenceAction" ):
                return visitor.visitSequenceAction(self)
            else:
                return visitor.visitChildren(self)




    def sequenceAction(self):

        localctx = WorkflowDslCoreParser.SequenceActionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_sequenceAction)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5 or _la==6:
                self.state = 47
                self.action()
                self.state = 52
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ActionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def syncAction(self):
            return self.getTypedRuleContext(WorkflowDslCoreParser.SyncActionContext,0)


        def getRuleIndex(self):
            return WorkflowDslCoreParser.RULE_action

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAction" ):
                return visitor.visitAction(self)
            else:
                return visitor.visitChildren(self)




    def action(self):

        localctx = WorkflowDslCoreParser.ActionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_action)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self.syncAction()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SyncActionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def function(self):
            return self.getTypedRuleContext(WorkflowDslCoreParser.FunctionContext,0)


        def NEWLINE(self):
            return self.getToken(WorkflowDslCoreParser.NEWLINE, 0)

        def Ignore(self):
            return self.getToken(WorkflowDslCoreParser.Ignore, 0)

        def getRuleIndex(self):
            return WorkflowDslCoreParser.RULE_syncAction

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSyncAction" ):
                return visitor.visitSyncAction(self)
            else:
                return visitor.visitChildren(self)




    def syncAction(self):

        localctx = WorkflowDslCoreParser.SyncActionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_syncAction)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 55
                self.match(WorkflowDslCoreParser.Ignore)


            self.state = 58
            self.function()
            self.state = 59
            self.match(WorkflowDslCoreParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(WorkflowDslCoreParser.ID, 0)

        def getRuleIndex(self):
            return WorkflowDslCoreParser.RULE_function

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction" ):
                return visitor.visitFunction(self)
            else:
                return visitor.visitChildren(self)




    def function(self):

        localctx = WorkflowDslCoreParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_function)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self.match(WorkflowDslCoreParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdentifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(WorkflowDslCoreParser.ID, 0)

        def getRuleIndex(self):
            return WorkflowDslCoreParser.RULE_identifier

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentifier" ):
                return visitor.visitIdentifier(self)
            else:
                return visitor.visitChildren(self)




    def identifier(self):

        localctx = WorkflowDslCoreParser.IdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self.match(WorkflowDslCoreParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





