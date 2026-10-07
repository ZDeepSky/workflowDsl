#include "step_engine.h"
static StepHost g_host = {0, 0};
void stepSetHost(const StepHost *host)
{
    if (host) g_host = *host;
    else { g_host.timerStart = 0; g_host.timerStop = 0; }
}
StepRet stepRun(Instance *inst, WORD32 msgId, void *msg, WORD32 len)
{
    (void)msgId;
    for (;;) {
        const Step *s = &inst->table[inst->idx];
        switch (s->kind) {
        case STEP_END:
            return STEP_RET_END;
        case STEP_CALL: {
            WORD32 r = s->func(inst, msg, len);
            if (r == STEP_OK) {
                inst->idx = s->next;
                continue;
            }
            inst->failCode = r;
            if (s->fail) { inst->idx = s->fail; continue; }
            return STEP_RET_FAIL;
        }
        case STEP_JUMPIF: {
            WORD32 r = s->func(inst, msg, len);
            if (r != 0) {                  /* 条件真 → 进分支体/循环体 */
                inst->idx = s->next;
            } else {                       /* 条件假 → 跳出 */
                inst->idx = s->jump;
            }
            continue;
        }
        /* 后续任务在此补 STEP_RECV / STEP_DELAY / STEP_ASYNC */
        default:
            return STEP_RET_FAIL;
        }
    }
}
StepRet stepResume(Instance *inst, WORD32 msgId, void *msg, WORD32 len)
{
    (void)inst; (void)msgId; (void)msg; (void)len;
    return STEP_RET_FAIL;  /* Task 4 实现 */
}
