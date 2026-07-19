# Generated from WorkflowDSL.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .WorkflowDSLParser import WorkflowDSLParser
else:
    from WorkflowDSLParser import WorkflowDSLParser

# This class defines a complete generic visitor for a parse tree produced by WorkflowDSLParser.

class WorkflowDSLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by WorkflowDSLParser#program.
    def visitProgram(self, ctx:WorkflowDSLParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WorkflowDSLParser#stepAlias.
    def visitStepAlias(self, ctx:WorkflowDSLParser.StepAliasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WorkflowDSLParser#conditionAlias.
    def visitConditionAlias(self, ctx:WorkflowDSLParser.ConditionAliasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WorkflowDSLParser#workflowDef.
    def visitWorkflowDef(self, ctx:WorkflowDSLParser.WorkflowDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WorkflowDSLParser#ActionStmt.
    def visitActionStmt(self, ctx:WorkflowDSLParser.ActionStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WorkflowDSLParser#SendStmt.
    def visitSendStmt(self, ctx:WorkflowDSLParser.SendStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WorkflowDSLParser#RecvStmt.
    def visitRecvStmt(self, ctx:WorkflowDSLParser.RecvStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WorkflowDSLParser#GotoStmt.
    def visitGotoStmt(self, ctx:WorkflowDSLParser.GotoStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WorkflowDSLParser#IfBlock.
    def visitIfBlock(self, ctx:WorkflowDSLParser.IfBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WorkflowDSLParser#WhileBlock.
    def visitWhileBlock(self, ctx:WorkflowDSLParser.WhileBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WorkflowDSLParser#FinalBlock.
    def visitFinalBlock(self, ctx:WorkflowDSLParser.FinalBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WorkflowDSLParser#actionBinding.
    def visitActionBinding(self, ctx:WorkflowDSLParser.ActionBindingContext):
        return self.visitChildren(ctx)



del WorkflowDSLParser