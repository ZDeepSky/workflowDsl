#include "workflows_gen.h"
#include "workflow_context.h"
#include "result_code.h"

#include <cstddef>

/*
 * Host-facing dispatch adapters.
 * Phase 6: legacy switch-case path removed; DSL mapping tables are the only route.
 */

#ifdef __cplusplus
extern "C" {
#endif

RetCode onReceiveMessage(WorkflowContext *t, void *msg, WORD32 len)
{
    if (t == NULL || t->action >= g_workflow_table_size) {
        return RC_FAIL;
    }
    WorkflowFunc entry = g_workflow_table[t->action];
    if (entry == NULL) {
        return RC_FAIL;
    }
    return entry(t, msg, len);
}

void onReceiveTokenResponse(WorkflowContext *t, void *msg, WORD32 len)
{
    if (t == NULL || t->action >= g_workflow_table_size) {
        return;
    }
    WorkflowResumeFunc resume = g_workflow_resume_table[t->action];
    if (resume != NULL) {
        resume(t, msg, len);
    }
}

void onReceiveProcessResult(WorkflowContext *t, void *msg, WORD32 len)
{
    onReceiveTokenResponse(t, msg, len);
}

void onReceiveTextResponse(WorkflowContext *t, void *msg, WORD32 len)
{
    onReceiveTokenResponse(t, msg, len);
}

void onReceiveQueryResponse(WorkflowContext *t, void *msg, WORD32 len)
{
    onReceiveTokenResponse(t, msg, len);
}

void onTimerDispatch(WorkflowContext *t, void *msg, WORD32 len)
{
    onReceiveTokenResponse(t, msg, len);
}

#ifdef __cplusplus
}
#endif
