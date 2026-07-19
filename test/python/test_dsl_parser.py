import sys
from pathlib import Path

from antlr4 import CommonTokenStream, InputStream

DISPATCH_DIR = Path(__file__).resolve().parent.parent.parent / "dispatch"
sys.path.insert(0, str(DISPATCH_DIR))

from WorkflowDSLLexer import WorkflowDSLLexer  # noqa: E402
from WorkflowDSLParser import WorkflowDSLParser  # noqa: E402
from gen_workflows import ModelBuilder  # noqa: E402


def parse_dsl(dsl_text):
    input_stream = InputStream(dsl_text)
    lexer = WorkflowDSLLexer(input_stream)# 词法分析器，将输入的文本转换为词法单元（token）
    tokens = CommonTokenStream(lexer)# 将词法单元转换为语法分析器可以理解的标记（token）
    parser = WorkflowDSLParser(tokens)# 语法分析器，将标记转换为抽象语法树（AST）
    tree = parser.program() # 语法分析器，将标记转换为抽象语法树（AST）
    visitor = ModelBuilder()# 访问者模式，用于遍历抽象语法树，生成模型
    visitor.visit(tree)
    return {
        "aliases": visitor.aliases,
        "conditions": visitor.conditions,
        "workflows": visitor.workflows,
        "bindings": visitor.bindings,
    }


# === @action 别名测试 ===

def test_parse_single_action_alias():
    model = parse_dsl("@action init = step_init")
    assert model["aliases"]["init"] == "step_init"


def test_parse_multiple_action_aliases():
    dsl = """
    @action init = step_init
    @action select_handler  = step_select_handler
    @action respond     = step_respond
    """
    model = parse_dsl(dsl)
    assert len(model["aliases"]) == 3
    assert model["aliases"]["select_handler"] == "step_select_handler"


# === @condition 别名测试 ===

def test_parse_condition_alias():
    model = parse_dsl("@condition isComplete = cond_isComplete")
    assert model["conditions"]["isComplete"] == "cond_isComplete"


# === workflow 定义测试 ===

def test_parse_minimal_workflow():
    dsl = """
    workflow Minimal
    {
        action  init
        final:
            action  cleanup
    }
    """
    model = parse_dsl(dsl)
    assert len(model["workflows"]) == 1
    workflow = model["workflows"][0]
    assert workflow["name"] == "Minimal"
    assert len(workflow["states"]) == 2
    assert workflow["states"][0] == {"type": "action", "name": "init"}
    assert workflow["states"][1]["type"] == "final"


def test_workflow_with_send_recv():
    dsl = """
    workflow Stream
    {
        send    send_request
        recv    recv_response
    }
    """
    model = parse_dsl(dsl)
    workflow = model["workflows"][0]
    assert workflow["states"][0] == {"type": "send", "name": "send_request"}
    assert workflow["states"][1] == {"type": "recv", "name": "recv_response"}


def test_workflow_with_if_block():
    dsl = """
    workflow WithGuard
    {
        action  select_handler
        if needValidate:
            action  validate
        action  respond
    }
    """
    model = parse_dsl(dsl)
    workflow = model["workflows"][0]
    assert workflow["states"][1]["type"] == "if"
    assert workflow["states"][1]["condition"] == "cond_needValidate"
    assert len(workflow["states"][1]["body"]) == 1
    assert workflow["states"][1]["body"][0] == {"type": "action", "name": "validate"}
    assert workflow["states"][2] == {"type": "action", "name": "respond"}


def test_workflow_with_while_loop():
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
    model = parse_dsl(dsl)
    workflow = model["workflows"][0]
    assert workflow["states"][2]["type"] == "while"
    assert workflow["states"][2]["condition"] == "cond_isComplete"
    assert len(workflow["states"][2]["body"]) == 1
    assert workflow["states"][2]["body"][0] == {"type": "goto", "target": "process_data"}


def test_workflow_with_goto():
    dsl = """
    workflow WithGoto
    {
        action  step_a
        goto step_c
        action  step_b
        action  step_c
    }
    """
    model = parse_dsl(dsl)
    workflow = model["workflows"][0]
    assert workflow["states"][1] == {"type": "goto", "target": "step_c"}


# === action 绑定测试 ===

def test_parse_action_binding():
    model = parse_dsl("action ACTION_STREAM_A = StreamFlow")
    assert len(model["bindings"]) == 1
    assert model["bindings"][0] == {
        "action": "ACTION_STREAM_A",
        "workflow": "StreamFlow",
    }


def test_multiple_actions_same_workflow():
    dsl = """
    action ACTION_A = FlowX
    action ACTION_B = FlowX
    action ACTION_C = FlowY
    """
    model = parse_dsl(dsl)
    assert len(model["bindings"]) == 3
    assert model["bindings"][0]["workflow"] == "FlowX"
    assert model["bindings"][1]["workflow"] == "FlowX"
    assert model["bindings"][2]["workflow"] == "FlowY"


# === 完整 DSL 文件测试 ===

def test_full_dsl_file():
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
    model = parse_dsl(dsl)
    assert len(model["aliases"]) == 2
    assert len(model["conditions"]) == 1
    assert len(model["workflows"]) == 1
    assert len(model["bindings"]) == 2


# === 边界情况 ===

def test_empty_file():
    model = parse_dsl("")
    assert len(model["workflows"]) == 0
    assert len(model["bindings"]) == 0


def test_comment_only_file():
    model = parse_dsl("// this is a comment\n// another line")
    assert len(model["workflows"]) == 0


def test_comment_inline():
    dsl = """
    // header comment
    @action init = step_init  // inline comment
    """
    model = parse_dsl(dsl)
    assert model["aliases"]["init"] == "step_init"
