# workflowDsl

DSL 工作流状态机模块：ANTLR 解析 → Jinja2 生成 C 状态表 → `step_engine` 运行。

## 构建库

```bash
cmake -S . -B build
cmake --build build -j$(nproc)
cmake --install build
```

产物：`output/lib/libworkflow_dsl.a`，头文件在 `output/include/workflow_dsl/`。

## 从 DSL 生成代码

```bash
cd dispatch
python3 gen_workflows.py workflows.dsl /tmp/wf_out
cp /tmp/wf_out/workflows_gen.h pub_inlcude/
cp /tmp/wf_out/workflows_gen.c source/
```

## 测试

```bash
# Python：解析器 14 + 代码生成 11
./test/python/run_tests.sh

# C++：引擎 / 步骤 / 集成
cmake -S test -B test/build && cmake --build test/build -j$(nproc)
./test/build/step_engine_ut
./test/build/step_impl_ut
./test/build/integration_ut
```

## 文档

| 文档 | 说明 |
|------|------|
| [docs/plan.md](docs/plan.md) | TDD 开发计划 |
| [docs/guide.md](docs/guide.md) | 架构详细讲解 |
| [docs/qa-exam.md](docs/qa-exam.md) | QA 考题 |
| [docs/commits/](docs/commits/) | 各 Commit 思路 |
