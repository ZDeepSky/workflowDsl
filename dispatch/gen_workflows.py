#!/usr/bin/env python3
"""DSL parser / code generator driver for workflow state machines."""

from WorkflowDSLVisitor import WorkflowDSLVisitor


class ModelBuilder(WorkflowDSLVisitor):
    def __init__(self):
        super().__init__()
        self.aliases = {}
        self.conditions = {}
        self.workflows = []
        self.bindings = []

    def _resolve_condition(self, name):
        return self.conditions.get(name, f"cond_{name}")

    def visitStepAlias(self, ctx):
        self.aliases[ctx.IDENT(0).getText()] = ctx.IDENT(1).getText()

    def visitConditionAlias(self, ctx):
        self.conditions[ctx.IDENT(0).getText()] = ctx.IDENT(1).getText()

    def visitWorkflowDef(self, ctx):
        name = ctx.IDENT().getText()
        states = [self.visit(s) for s in ctx.statement()]
        self.workflows.append({"name": name, "states": states})

    def visitActionStmt(self, ctx):
        return {"type": "action", "name": ctx.IDENT().getText()}

    def visitSendStmt(self, ctx):
        return {"type": "send", "name": ctx.IDENT().getText()}

    def visitRecvStmt(self, ctx):
        return {"type": "recv", "name": ctx.IDENT().getText()}

    def visitGotoStmt(self, ctx):
        return {"type": "goto", "target": ctx.IDENT().getText()}

    def visitIfBlock(self, ctx):
        return {
            "type": "if",
            "condition": self._resolve_condition(ctx.IDENT().getText()),
            "body": [self.visit(ctx.statement())],
        }

    def visitWhileBlock(self, ctx):
        return {
            "type": "while",
            "condition": self._resolve_condition(ctx.IDENT().getText()),
            "body": [self.visit(ctx.statement())],
        }

    def visitFinalBlock(self, ctx):
        return {
            "type": "final",
            "body": [self.visit(ctx.statement())],
        }

    def visitActionBinding(self, ctx):
        self.bindings.append(
            {
                "action": ctx.IDENT(0).getText(),
                "workflow": ctx.IDENT(1).getText(),
            }
        )
