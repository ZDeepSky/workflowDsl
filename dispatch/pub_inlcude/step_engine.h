#pragma once

#include "types.h"

typedef enum {
    STEP_RET_OK    = 0,
    STEP_RET_WAIT,
    STEP_RET_END,
    STEP_RET_ERROR,
} StepRet;

typedef struct {
    WORD32 idx;
    WORD32 nextIdx;
} StepContext;

typedef StepRet (*StepFunc)(void *workflow, void *msg, WORD32 len, StepContext *ctx);

typedef struct {
    StepFunc func;
    const char *name;
} StateEntry;

struct WorkflowContext;

#ifdef __cplusplus
extern "C" {
#endif

void stepRun(void *workflow, void *msg, WORD32 len);
void stepResume(void *workflow, void *msg, WORD32 len);

#ifdef __cplusplus
}
#endif
