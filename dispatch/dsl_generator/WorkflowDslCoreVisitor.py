# Generated from WorkflowDslCore.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .WorkflowDslCoreParser import WorkflowDslCoreParser
else:
    from WorkflowDslCoreParser import WorkflowDslCoreParser

# This class defines a complete generic visitor for a parse tree produced by WorkflowDslCoreParser.

class WorkflowDslCoreVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by WorkflowDslCoreParser#workflowFile.
    def visitWorkflowFile(self, ctx:WorkflowDslCoreParser.WorkflowFileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WorkflowDslCoreParser#workflow.
    def visitWorkflow(self, ctx:WorkflowDslCoreParser.WorkflowContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WorkflowDslCoreParser#procedure.
    def visitProcedure(self, ctx:WorkflowDslCoreParser.ProcedureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WorkflowDslCoreParser#procedureBody.
    def visitProcedureBody(self, ctx:WorkflowDslCoreParser.ProcedureBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WorkflowDslCoreParser#sequenceAction.
    def visitSequenceAction(self, ctx:WorkflowDslCoreParser.SequenceActionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WorkflowDslCoreParser#action.
    def visitAction(self, ctx:WorkflowDslCoreParser.ActionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WorkflowDslCoreParser#syncAction.
    def visitSyncAction(self, ctx:WorkflowDslCoreParser.SyncActionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WorkflowDslCoreParser#function.
    def visitFunction(self, ctx:WorkflowDslCoreParser.FunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WorkflowDslCoreParser#identifier.
    def visitIdentifier(self, ctx:WorkflowDslCoreParser.IdentifierContext):
        return self.visitChildren(ctx)



del WorkflowDslCoreParser