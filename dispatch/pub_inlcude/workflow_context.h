#pragma once

#include "types.h"

#ifdef __cplusplus
extern "C" {
#endif

/* 旧平坦状态表用的上下文。新引擎走 Instance，不使用这两个类型。 */
typedef struct {
    WORD32 idx;
    WORD32 nextIdx;
} StepContext;

typedef int (*LegacyStepFn)(void *workflow, void *msg, WORD32 len, StepContext *ctx);

typedef struct {
    LegacyStepFn func;
    const char *name;
} StateEntry;

typedef struct WorkflowContext {
    StepContext step;
    StateEntry *stateTable;
    WORD32 ctxId;
    WORD32 action;
    /* 1 = current recv/send step already suspended once; resume should proceed */
    WORD32 waitArmed;
} WorkflowContext;

#ifdef __cplusplus
}
#endif
