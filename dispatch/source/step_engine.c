#include "step_engine.h"

#include <stddef.h>

typedef struct {
    StepContext step;
    StateEntry *stateTable;
    int callCount;
} TestWorkflowCtx;

void stepRun(void *workflow, void *msg, WORD32 len)
{
    StepContext *ctx = (StepContext *)((char *)workflow + offsetof(TestWorkflowCtx, step));
    StateEntry *table = *(StateEntry **)((char *)workflow + offsetof(TestWorkflowCtx, stateTable));

    while (1) {
        StateEntry *entry = &table[ctx->idx];
        if (!entry->func) {
            return;
        }

        ctx->nextIdx = ctx->idx + 1;
        StepRet ret = entry->func(workflow, msg, len, ctx);

        switch (ret) {
        case STEP_RET_OK:
            ctx->idx = ctx->nextIdx;
            continue;
        case STEP_RET_WAIT:
            return;
        case STEP_RET_END:
            return;
        case STEP_RET_ERROR:
            return;
        }
    }
}

void stepResume(void *workflow, void *msg, WORD32 len)
{
    stepRun(workflow, msg, len);
}
