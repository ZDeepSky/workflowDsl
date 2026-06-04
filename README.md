# workflowDsl

DSL 工作流状态机模块。开发计划见 [docs/plan.md](docs/plan.md)。

## 构建与测试

```bash
cmake -S . -B test/build
cmake --build test/build -j$(nproc)
ctest --test-dir test/build --output-on-failure
```

或直接运行：

```bash
./test/build/step_engine_ut
```
