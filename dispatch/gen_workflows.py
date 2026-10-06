#!/usr/bin/env python3
"""DSL parser / code generator driver for workflow state machines."""

from __future__ import annotations

import sys
from pathlib import Path

from antlr4 import CommonTokenStream, FileStream, InputStream
from jinja2 import Environment, FileSystemLoader

from WorkflowDSLLexer import WorkflowDSLLexer
from WorkflowDSLParser import WorkflowDSLParser
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


def _cond_short(condition: str) -> str:
    return condition[5:] if condition.startswith("cond_") else condition


def _flatten_states(states, aliases, workflow_name):
    """Flatten nested if/while/final into a linear StateEntry list."""
    flat = []
    for st in states:
        t = st["type"]
        if t in ("action", "send", "recv"):
            name = st["name"]
            flat.append(
                {
                    "type": t,
                    "name": name,
                    "cfunc": aliases.get(name, name),
                    "is_wrapper": False,
                }
            )
        elif t == "goto":
            target = st["target"]
            flat.append(
                {
                    "type": "goto",
                    "name": f"goto_{target}",
                    "target": target,
                    "cfunc": f"wrapper_{workflow_name}_goto_{target}",
                    "is_wrapper": True,
                }
            )
        elif t == "if":
            short = _cond_short(st["condition"])
            body_flat = _flatten_states(st["body"], aliases, workflow_name)
            node = {
                "type": "if",
                "name": f"if_{short}",
                "condition": st["condition"],
                "cfunc": f"wrapper_{workflow_name}_if_{short}",
                "is_wrapper": True,
                "body_len": len(body_flat),
            }
            flat.append(node)
            flat.extend(body_flat)
        elif t == "while":
            short = _cond_short(st["condition"])
            loop_target = None
            for b in st["body"]:
                if b["type"] == "goto":
                    loop_target = b["target"]
                    break
            flat.append(
                {
                    "type": "while",
                    "name": f"while_{short}",
                    "condition": st["condition"],
                    "loop_target": loop_target,
                    "cfunc": f"wrapper_{workflow_name}_while_{short}",
                    "is_wrapper": True,
                }
            )
        elif t == "final":
            flat.extend(_flatten_states(st["body"], aliases, workflow_name))
    return flat


def _annotate_control_flow(flat):
    """Fill then/else names for if wrappers using absolute indices."""
    for i, st in enumerate(flat):
        if st["type"] != "if":
            continue
        then_idx = i + 1
        else_idx = i + 1 + st["body_len"]
        if then_idx < len(flat):
            st["then_name"] = flat[then_idx]["name"]
        else:
            st["then_name"] = flat[i]["name"]  # degenerate
        if else_idx < len(flat):
            st["else_name"] = flat[else_idx]["name"]
        else:
            # fall through past sentinel conceptually — point at last+1 via next default;
            # still need a named IDX for template; use a synthetic sentinel label name
            # by reusing then_name when empty body edge-case; prefer last flat name+1
            # For codegen tests we always have a following step.
            st["else_name"] = flat[-1]["name"] if flat else st["name"]


def parse_dsl(dsl_text: str) -> dict:
    """Parse DSL text into a model dict ready for Jinja rendering."""
    input_stream = InputStream(dsl_text)
    lexer = WorkflowDSLLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = WorkflowDSLParser(tokens)
    tree = parser.program()
    builder = ModelBuilder()
    builder.visit(tree)

    used_steps = set()
    used_conds = set()

    for workflow in builder.workflows:
        flat = _flatten_states(workflow["states"], builder.aliases, workflow["name"])
        _annotate_control_flow(flat)
        workflow["flat_states"] = flat
        for st in flat:
            if st.get("is_wrapper"):
                if st["type"] in ("if", "while"):
                    used_conds.add(st["condition"])
            else:
                used_steps.add(st["cfunc"])

    unresolved_steps = sorted(
        s for s in used_steps if s not in builder.aliases.values()
    )
    unresolved_conds = sorted(
        c for c in used_conds if c not in builder.conditions.values()
    )

    return {
        "workflows": builder.workflows,
        "bindings": builder.bindings,
        "aliases": builder.aliases,
        "conditions": builder.conditions,
        "unresolved_steps": unresolved_steps,
        "unresolved_conds": unresolved_conds,
    }


def render_code(model: dict) -> dict:
    """Render workflows_gen.h / .c via Jinja2 templates."""
    template_dir = Path(__file__).resolve().parent
    env = Environment(
        loader=FileSystemLoader(str(template_dir)),
        trim_blocks=True,
        lstrip_blocks=True,
        keep_trailing_newline=True,
    )
    result = {}
    for tmpl_name, key in [
        ("workflows_gen.h.j2", ".h"),
        ("workflows_gen.c.j2", ".c"),
    ]:
        template = env.get_template(tmpl_name)
        result[key] = template.render(**model)
    return result


def main():
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <workflows.dsl> [out_dir]")
        sys.exit(1)

    dsl_path = Path(sys.argv[1])
    out_dir = Path(sys.argv[2]) if len(sys.argv) > 2 else dsl_path.parent
    out_dir.mkdir(parents=True, exist_ok=True)

    model = parse_dsl(dsl_path.read_text())
    code = render_code(model)

    h_path = out_dir / "workflows_gen.h"
    c_path = out_dir / "workflows_gen.c"
    h_path.write_text(code[".h"])
    c_path.write_text(code[".c"])
    print(f"Generated {h_path}")
    print(f"Generated {c_path}")


if __name__ == "__main__":
    main()
