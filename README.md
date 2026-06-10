# workflowDsl

DSL 工作流状态机模块。

## 构建库

生成 `output/lib/libworkflow_dsl.a`，并将公开头文件拷贝到 `output/include/`：

```bash
cmake -S . -B build
cmake --build build -j$(nproc)
```

## 构建与测试

```bash
cmake -S test -B test/build
cmake --build test/build -j$(nproc)
ctest --test-dir test/build --output-on-failure
```

或直接运行：

```bash
./test/build/step_engine_ut
```
