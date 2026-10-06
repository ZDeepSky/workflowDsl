#include "step_engine.h"
#include "workflow_context.h"
#include "host_api.h"
#include "result_code.h"

#include <cstddef>

/* Test/host override: 1 = complete, 0 = keep looping */
int g_cond_is_complete = 1;

extern "C" {

StepRet step_init(WorkflowContext *t, void *m, WORD32 l, StepContext *ctx)
{
    (void)t;
    (void)m;
    (void)l;
    (void)ctx;
    return STEP_RET_OK;
}

StepRet step_select_handler(WorkflowContext *t, void *m, WORD32 l, StepContext *ctx)
{
    (void)t;
    (void)m;
    (void)l;
    (void)ctx;
    return STEP_RET_OK;
}

StepRet step_process_data(WorkflowContext *t, void *m, WORD32 l, StepContext *ctx)
{
    (void)m;
    (void)l;
    (void)ctx;
    /* recv: first entry suspends; resume after host callback continues */
    if (!t->waitArmed) {
        t->waitArmed = 1;
        return STEP_RET_WAIT;
    }
    t->waitArmed = 0;
    return STEP_RET_OK;
}

StepRet step_respond(WorkflowContext *t, void *m, WORD32 l, StepContext *ctx)
{
    (void)ctx;
    if (sendResponse(t, m, l) != RC_SUCCESS) {
        return STEP_RET_ERROR;
    }
    return STEP_RET_OK;
}

StepRet step_cleanup(WorkflowContext *t, void *m, WORD32 l, StepContext *ctx)
{
    (void)m;
    (void)l;
    (void)ctx;
    deleteWorkflowContext(t);
    return STEP_RET_END;
}

int cond_isComplete(WorkflowContext *t, void *m, WORD32 l, StepContext *ctx)
{
    (void)t;
    (void)m;
    (void)l;
    (void)ctx;
    return g_cond_is_complete;
}

}  // extern "C"
