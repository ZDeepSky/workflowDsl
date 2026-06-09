#include "TestFramework.h"
#include "step_engine.h"

struct TestWorkflowCtx {
    StepContext step;
    StateEntry *stateTable;
    int callCount;
};

static StepRet mock_ok(TestWorkflowCtx *t, void *m, WORD32 l, StepContext *ctx) {
    (void)m;
    (void)l;
    (void)ctx;
    t->callCount++;
    return STEP_RET_OK;
}

TEST(StepEngine, linear_three_steps_then_sentinel_stops)
{
    TestWorkflowCtx workflow = {};
    StateEntry table[] = {
        { (StepFunc)mock_ok, "step1" },
        { (StepFunc)mock_ok, "step2" },
        { (StepFunc)mock_ok, "step3" },
        { NULL, NULL },
    };
    workflow.stateTable = table;

    stepRun(&workflow, NULL, 0);

    EXPECT_EQ(workflow.callCount, 3);
    EXPECT_EQ(workflow.step.idx, 3u);
}

static int waitCount = 0;

static StepRet mock_wait_then_ok(TestWorkflowCtx *t, void *m, WORD32 l, StepContext *ctx) {
    (void)m;
    (void)l;
    (void)ctx;
    t->callCount++;
    if (waitCount++ == 0) return STEP_RET_WAIT;
    return STEP_RET_OK;
}

TEST(StepEngine, wait_suspends_and_resume_continues)
{
    waitCount = 0;
    TestWorkflowCtx workflow = {};
    StateEntry table[] = {
        { (StepFunc)mock_ok,          "before_wait" },
        { (StepFunc)mock_wait_then_ok, "wait_step"  },
        { (StepFunc)mock_ok,          "after_wait"  },
        { NULL, NULL },
    };
    workflow.stateTable = table;

    stepRun(&workflow, NULL, 0);
    EXPECT_EQ(workflow.callCount, 2);
    EXPECT_EQ(workflow.step.idx, 1u);

    stepResume(&workflow, NULL, 0);
    EXPECT_EQ(workflow.callCount, 4);  // wait_step 再次调用 + after_wait
    EXPECT_EQ(workflow.step.idx, 3u);
}

static StepRet mock_error(TestWorkflowCtx *t, void *m, WORD32 l, StepContext *ctx) {
    (void)m;
    (void)l;
    (void)ctx;
    t->callCount++;
    return STEP_RET_ERROR;
}

TEST(StepEngine, error_stops_engine_and_does_not_continue)
{
    TestWorkflowCtx workflow = {};
    StateEntry table[] = {
        { (StepFunc)mock_ok,    "step1" },
        { (StepFunc)mock_error, "bad_step" },
        { (StepFunc)mock_ok,    "never_reached" },
        { NULL, NULL },
    };
    workflow.stateTable = table;

    stepRun(&workflow, NULL, 0);

    EXPECT_EQ(workflow.callCount, 2);
}

static StepRet mock_end(TestWorkflowCtx *t, void *m, WORD32 l, StepContext *ctx) {
    (void)m;
    (void)l;
    (void)ctx;
    t->callCount++;
    return STEP_RET_END;
}

TEST(StepEngine, end_stops_engine_normally)
{
    TestWorkflowCtx workflow = {};
    StateEntry table[] = {
        { (StepFunc)mock_ok,  "step1" },
        { (StepFunc)mock_end, "final_step" },
        { (StepFunc)mock_ok,  "never_reached" },
        { NULL, NULL },
    };
    workflow.stateTable = table;

    stepRun(&workflow, NULL, 0);

    EXPECT_EQ(workflow.callCount, 2);
}

static StepRet mock_goto_step3(TestWorkflowCtx *t, void *m, WORD32 l, StepContext *ctx) {
    (void)m;
    (void)l;
    t->callCount++;
    ctx->nextIdx = 2;
    return STEP_RET_OK;
}

TEST(StepEngine, nextidx_override_jumps_to_target)
{
    TestWorkflowCtx workflow = {};
    StateEntry table[] = {
        { (StepFunc)mock_ok,         "step1" },
        { (StepFunc)mock_goto_step3, "goto_step" },
        { (StepFunc)mock_ok,         "step3" },
        { (StepFunc)mock_ok,         "step4" },
        { NULL, NULL },
    };
    workflow.stateTable = table;

    stepRun(&workflow, NULL, 0);

    EXPECT_EQ(workflow.callCount, 4);
}

TEST(StepEngine, empty_table_immediately_stops)
{
    TestWorkflowCtx workflow = {};
    StateEntry table[] = {
        { NULL, NULL },
    };
    workflow.stateTable = table;

    stepRun(&workflow, NULL, 0);

    EXPECT_EQ(workflow.callCount, 0);
}

static StepRet mock_wait_then_error(TestWorkflowCtx *t, void *m, WORD32 l, StepContext *ctx) {
    (void)m;
    (void)l;
    (void)ctx;
    t->callCount++;
    if (t->callCount == 1) return STEP_RET_WAIT;
    return STEP_RET_ERROR;
}

TEST(StepEngine, wait_then_error_on_resume_stops)
{
    TestWorkflowCtx workflow = {};
    StateEntry table[] = {
        { (StepFunc)mock_wait_then_error, "flaky_step" },
        { (StepFunc)mock_ok,              "never_reached" },
        { NULL, NULL },
    };
    workflow.stateTable = table;

    stepRun(&workflow, NULL, 0);
    EXPECT_EQ(workflow.callCount, 1);
    EXPECT_EQ(workflow.step.idx, 0u);

    stepResume(&workflow, NULL, 0);
    EXPECT_EQ(workflow.callCount, 2);
}
