#include "TestFramework.h"
#include "step_engine.h"

namespace {

const char *g_trace[64];
int         g_traceN;

WORD32 fn_A(Instance*, void*, WORD32) { g_trace[g_traceN++] = "A"; return STEP_OK; }
WORD32 fn_B(Instance*, void*, WORD32) { g_trace[g_traceN++] = "B"; return STEP_OK; }
WORD32 fn_C(Instance*, void*, WORD32) { g_trace[g_traceN++] = "C"; return STEP_OK; }
WORD32 fn_fail(Instance*, void*, WORD32) { g_trace[g_traceN++] = "X"; return STEP_FAIL; }
WORD32 fn_fail9(Instance*, void*, WORD32) { g_trace[g_traceN++] = "9"; return 9; }

Step S_CALL(StepFunc f, WORD32 next, WORD32 fail) {
    Step s = {0};
    s.kind = STEP_CALL; s.func = f; s.next = next; s.fail = fail;
    return s;
}
Step S_END() {
    Step s = {0}; s.kind = STEP_END; return s;
}

void fresh(Instance *inst, const Step *table) {
    inst->table = table; inst->idx = 0; inst->failCode = 0; inst->userCtx = 0;
    for (int i = 0; i < MAX_LOOP_NEST; i++) inst->loopCount[i] = 0;
}

void clearTrace() {
    g_traceN = 0;
    for (int i = 0; i < 64; i++) g_trace[i] = nullptr;
}

}  // namespace

class StepEngine : public ::testing::Test {
protected:
    void SetUp() override
    {
        clearTrace();
    }

    void TearDown() override
    {
        clearTrace();
    }
};

TEST_F(StepEngine, linear_three_steps_then_end)
{
    Step table[] = { S_CALL(fn_A, 1, 0), S_CALL(fn_B, 2, 0), S_CALL(fn_C, 3, 0), S_END() };
    Instance inst; fresh(&inst, table);
    StepRet r = stepRun(&inst, 0, 0, 0);
    EXPECT_EQ(r, STEP_RET_END);
    EXPECT_EQ(inst.idx, 3u);
    EXPECT_STREQ(g_trace[0], "A");
    EXPECT_STREQ(g_trace[1], "B");
    EXPECT_STREQ(g_trace[2], "C");
}

TEST_F(StepEngine, fail_without_fail_target_stops)
{
    Step table[] = { S_CALL(fn_A, 1, 0), S_CALL(fn_fail, 2, 0), S_CALL(fn_B, 3, 0), S_END() };
    Instance inst; fresh(&inst, table);
    StepRet r = stepRun(&inst, 0, 0, 0);
    EXPECT_EQ(r, STEP_RET_FAIL);
    EXPECT_EQ(inst.failCode, 1u);
    EXPECT_EQ(g_traceN, 2);            // A, X —— B 未执行
}

TEST_F(StepEngine, fail_jumps_to_fail_block_and_keeps_failcode)
{
    // 排布 [0..1 正常][2 fail 块][3 finally][4 END]
    Step table[] = {
        S_CALL(fn_A,    1, 2),   // 0 正常，失败→2
        S_CALL(fn_fail9, 3, 2),  // 1 失败码=9，失败→2
        S_CALL(fn_B,    3, 0),   // 2 fail 块 → finally(3)
        S_CALL(fn_C,    4, 0),   // 3 finally → END
        S_END(),                 // 4
    };
    Instance inst; fresh(&inst, table);
    StepRet r = stepRun(&inst, 0, 0, 0);
    EXPECT_EQ(r, STEP_RET_END);
    EXPECT_EQ(inst.failCode, 9u);      // 失败码保留
    EXPECT_STREQ(g_trace[0], "A");
    EXPECT_STREQ(g_trace[1], "9");
    EXPECT_STREQ(g_trace[2], "B");     // fail 块
    EXPECT_STREQ(g_trace[3], "C");     // finally
    EXPECT_EQ(g_traceN, 4);
}
