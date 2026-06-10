import sys
import unittest
from pathlib import Path

from antlr4 import CommonTokenStream, InputStream

DISPATCH_DIR = Path(__file__).resolve().parent.parent.parent / "dispatch"
sys.path.insert(0, str(DISPATCH_DIR))

from WorkflowDSLLexer import WorkflowDSLLexer  # noqa: E402
from WorkflowDSLParser import WorkflowDSLParser  # noqa: E402
from gen_workflows import ModelBuilder  # noqa: E402


class TestDslParser(unittest.TestCase):

    def _parse(self, dsl_text):
        input_stream = InputStream(dsl_text)
        lexer = WorkflowDSLLexer(input_stream)
        tokens = CommonTokenStream(lexer)
        parser = WorkflowDSLParser(tokens)
        tree = parser.program()
        visitor = ModelBuilder()
        visitor.visit(tree)
        return {
            "aliases": visitor.aliases,
            "conditions": visitor.conditions,
            "workflows": visitor.workflows,
            "bindings": visitor.bindings,
        }

    # === @action 别名测试 ===

    def test_parse_single_action_alias(self):
        model = self._parse("@action init = step_init")
        self.assertEqual(model["aliases"]["init"], "step_init")

    def test_parse_multiple_action_aliases(self):
        dsl = """
        @action init = step_init
        @action select_handler  = step_select_handler
        @action respond     = step_respond
        """
        model = self._parse(dsl)
        self.assertEqual(len(model["aliases"]), 3)
        self.assertEqual(model["aliases"]["select_handler"], "step_select_handler")

    # === @condition 别名测试 ===

    def test_parse_condition_alias(self):
        model = self._parse("@condition isComplete = cond_isComplete")
        self.assertEqual(model["conditions"]["isComplete"], "cond_isComplete")

    # === workflow 定义测试 ===

    def test_parse_minimal_workflow(self):
        dsl = """
        workflow Minimal
        {
            action  init
            final:
                action  cleanup
        }
        """
        model = self._parse(dsl)
        self.assertEqual(len(model["workflows"]), 1)
        workflow = model["workflows"][0]
        self.assertEqual(workflow["name"], "Minimal")
        self.assertEqual(len(workflow["states"]), 2)
        self.assertEqual(workflow["states"][0], {"type": "action", "name": "init"})
        self.assertEqual(workflow["states"][1]["type"], "final")

    def test_workflow_with_send_recv(self):
        dsl = """
        workflow Stream
        {
            send    send_request
            recv    recv_response
        }
        """
        model = self._parse(dsl)
        workflow = model["workflows"][0]
        self.assertEqual(workflow["states"][0], {"type": "send", "name": "send_request"})
        self.assertEqual(workflow["states"][1], {"type": "recv", "name": "recv_response"})

    def test_workflow_with_if_block(self):
        dsl = """
        workflow WithGuard
        {
            action  select_handler
            if needValidate:
                action  validate
            action  respond
        }
        """
        model = self._parse(dsl)
        workflow = model["workflows"][0]
        self.assertEqual(workflow["states"][1]["type"], "if")
        self.assertEqual(workflow["states"][1]["condition"], "cond_needValidate")
        self.assertEqual(len(workflow["states"][1]["body"]), 1)
        self.assertEqual(workflow["states"][1]["body"][0], {"type": "action", "name": "validate"})
        self.assertEqual(workflow["states"][2], {"type": "action", "name": "respond"})

    def test_workflow_with_while_loop(self):
        dsl = """
        workflow LoopFlow
        {
            action  select_handler
            recv    process_data
            while not isComplete:
                goto process_data
            final:
                action  cleanup
        }
        """
        model = self._parse(dsl)
        workflow = model["workflows"][0]
        self.assertEqual(workflow["states"][2]["type"], "while")
        self.assertEqual(workflow["states"][2]["condition"], "cond_isComplete")
        self.assertEqual(len(workflow["states"][2]["body"]), 1)
        self.assertEqual(workflow["states"][2]["body"][0], {"type": "goto", "target": "process_data"})

    def test_workflow_with_goto(self):
        dsl = """
        workflow WithGoto
        {
            action  step_a
            goto step_c
            action  step_b
            action  step_c
        }
        """
        model = self._parse(dsl)
        workflow = model["workflows"][0]
        self.assertEqual(workflow["states"][1], {"type": "goto", "target": "step_c"})

    # === action 绑定测试 ===

    def test_parse_action_binding(self):
        model = self._parse("action ACTION_STREAM_A = StreamFlow")
        self.assertEqual(len(model["bindings"]), 1)
        self.assertEqual(
            model["bindings"][0],
            {"action": "ACTION_STREAM_A", "workflow": "StreamFlow"},
        )

    def test_multiple_actions_same_workflow(self):
        dsl = """
        action ACTION_A = FlowX
        action ACTION_B = FlowX
        action ACTION_C = FlowY
        """
        model = self._parse(dsl)
        self.assertEqual(len(model["bindings"]), 3)
        self.assertEqual(model["bindings"][0]["workflow"], "FlowX")
        self.assertEqual(model["bindings"][1]["workflow"], "FlowX")
        self.assertEqual(model["bindings"][2]["workflow"], "FlowY")

    # === 完整 DSL 文件测试 ===

    def test_full_dsl_file(self):
        dsl = """
        @action init       = step_init
        @action select_handler        = step_select_handler
        @condition isComplete      = cond_isComplete

        workflow SimpleFlow
        {
            action  init
            action  select_handler
            recv    process_data
            action  respond
            while not isComplete:
                goto process_data
            final:
                action  cleanup
        }

        action ACTION_SIMPLE_A = SimpleFlow
        action ACTION_SIMPLE_B     = SimpleFlow
        """
        model = self._parse(dsl)
        self.assertEqual(len(model["aliases"]), 2)
        self.assertEqual(len(model["conditions"]), 1)
        self.assertEqual(len(model["workflows"]), 1)
        self.assertEqual(len(model["bindings"]), 2)

    # === 边界情况 ===

    def test_empty_file(self):
        model = self._parse("")
        self.assertEqual(len(model["workflows"]), 0)
        self.assertEqual(len(model["bindings"]), 0)

    def test_comment_only_file(self):
        model = self._parse("// this is a comment\n// another line")
        self.assertEqual(len(model["workflows"]), 0)

    def test_comment_inline(self):
        dsl = """
        // header comment
        @action init = step_init  // inline comment
        """
        model = self._parse(dsl)
        self.assertEqual(model["aliases"]["init"], "step_init")


if __name__ == "__main__":
    unittest.main()
