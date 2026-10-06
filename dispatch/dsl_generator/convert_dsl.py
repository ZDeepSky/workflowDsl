#!/usr/bin/env python3
"""把 WorkflowDslCore 文本转成流程列表。

当前只认识同步动作：一行一个函数名，可选 ignore。
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

from antlr4 import CommonTokenStream, InputStream
from antlr4.error.ErrorListener import ErrorListener

from WorkflowDslCoreLexer import WorkflowDslCoreLexer
from WorkflowDslCoreParser import WorkflowDslCoreParser
from WorkflowDslCoreVisitor import WorkflowDslCoreVisitor


class _SyntaxError(ErrorListener):
    def __init__(self):
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.errors.append(f"{line}:{column} {msg}")


class ModelBuilder(WorkflowDslCoreVisitor):
    def __init__(self):
        super().__init__()
        self.workflows = []
        self.procedures = []

    def visitWorkflow(self, ctx):
        self.workflows.append(self._flow("workflow", ctx.procedureBody()))
        return None

    def visitProcedure(self, ctx):
        self.procedures.append(self._flow("procedure", ctx.procedureBody()))
        return None

    def _flow(self, kind, body):
        actions = []
        for action in body.sequenceAction().action():
            sync = action.syncAction()
            actions.append(
                {
                    "name": sync.function().ID().getText(),
                    "ignore": sync.Ignore() is not None,
                }
            )
        return {
            "kind": kind,
            "name": body.identifier().ID().getText(),
            "actions": actions,
        }


def parse_dsl(text: str) -> dict:
    lexer = WorkflowDslCoreLexer(InputStream(text))
    lexer.removeErrorListeners()
    lex_errors = _SyntaxError()
    lexer.addErrorListener(lex_errors)

    parser = WorkflowDslCoreParser(CommonTokenStream(lexer))
    parser.removeErrorListeners()
    parse_errors = _SyntaxError()
    parser.addErrorListener(parse_errors)

    tree = parser.workflowFile()
    errors = lex_errors.errors + parse_errors.errors
    if errors:
        raise SyntaxError("\n".join(errors))

    builder = ModelBuilder()
    builder.visit(tree)
    return {"workflows": builder.workflows, "procedures": builder.procedures}


def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <file.dsl>", file=sys.stderr)
        sys.exit(1)
    text = Path(sys.argv[1]).read_text(encoding="utf-8")
    print(json.dumps(parse_dsl(text), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
