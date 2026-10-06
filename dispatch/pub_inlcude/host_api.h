#pragma once

#include "types.h"
#include "result_code.h"
#include "workflow_context.h"

#ifdef __cplusplus
extern "C" {
#endif

RetCode sendResponse(WorkflowContext *t, void *msg, WORD32 len);
BOOLEAN deleteWorkflowContext(WorkflowContext *t);

/* Optional host/test knob for while-not-complete loops */
extern int g_cond_is_complete;

#ifdef __cplusplus
}
#endif
