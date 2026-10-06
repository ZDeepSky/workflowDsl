#pragma once
#include "types.h"
#ifdef __cplusplus
extern "C" {
#endif
/* ---- 引擎返回码 ---- */
typedef enum {
    STEP_RET_OK      = 0,
    STEP_RET_WAIT    = 1,
    STEP_RET_FAIL    = 2,
    STEP_RET_END     = 3,
    STEP_RET_UNKNOWN = 4,
    STEP_RET_ERROR   = STEP_RET_FAIL, /* 旧宿主桩仍返回此名 */
} StepRet;
/* ---- 用户函数返回值（动作=状态码 / delay=时长 / 条件=0|非0） ---- */
enum {
    STEP_OK      = 0,
    STEP_FAIL    = 1,
    STEP_WAIT    = 2,
    STEP_INVALID = 0xFFFFFFFFu,   /* delay 返回值无效 */
};
#define STEP_DEAD_LOOP 0x7FFFFFFEu  /* 死循环失败码 */
/* 定时器消息 id 约定：高 4 位标记 + 低 28 位 = 步骤下标 */
#define TIMER_MSG_BASE  0xE0000000u
#define TIMER_MSG(idx)  (TIMER_MSG_BASE | (WORD32)(idx))
#define IS_TIMER_MSG(m) (((m) & TIMER_MSG_BASE) == TIMER_MSG_BASE)
#define TIMER_STEP(m)   ((m) & ~TIMER_MSG_BASE)
typedef struct Step     Step;
typedef struct Instance Instance;
/* 用户函数指针。返回值按槽位解释：
   CALL/ASYNC/RECV-handler = 状态码；DELAY = 时长；JUMPIF = 条件(0假/非0真)。 */
typedef WORD32 (*StepFunc)(Instance *inst, void *msg, WORD32 len);
/* ---- 指令类型 ---- */
enum {
    STEP_CALL = 0,   /* 调用 func；STEP_OK→next，非0→fail */
    STEP_ASYNC,      /* 发请求；STEP_WAIT→next(receive)，STEP_OK→jump(跳过 receive) */
    STEP_RECV,       /* 挂起等消息（分支表 + 可选 after 超时） */
    STEP_DELAY,      /* func 返回时长；0→next，>0 挂起定时器，INVALID→fail */
    STEP_JUMPIF,     /* func 为条件；真→next，假→jump；max>0 时做循环计数 */
    STEP_END,        /* 流程结束 */
};
/* receive 分支 */
typedef struct {
    WORD32   msg;      /* 期望消息 id */
    StepFunc handler;  /* 命中后调用 */
    WORD32   next;     /* handler 成功后的下一步 */
} RecvBranch;
struct Step {
    WORD32     kind;
    StepFunc   func;
    WORD32     next;           /* 正常下一步 */
    WORD32     jump;           /* JUMPIF 假跳 / ASYNC 跳过 receive */
    WORD32     fail;           /* 失败跳转（0=无，直接 FAIL 结束） */
    WORD32     msg;            /* RECV: after 超时时长（0=无超时） */
    WORD32     timeoutNext;    /* RECV 超时后下一步 */
    StepFunc   timeoutHandler; /* RECV 超时处理函数（可空） */
    RecvBranch *recv;          /* RECV 分支表 */
    WORD32     recvNum;        /* 分支数 */
    WORD32     loopId;         /* 循环计数器槽位（JUMPIF 且 max>0 时用） */
    WORD32     max;            /* 循环上限（0=非循环） */
};
#define MAX_LOOP_NEST 16
struct Instance {
    const Step *table;                 /* 指令表 */
    WORD32      idx;                   /* 当前指令（挂起时停在这） */
    WORD32      failCode;              /* 当前失败码 */
    void       *userCtx;               /* 用户上下文 */
    WORD32      loopCount[MAX_LOOP_NEST];  /* 循环计数 */
};
/* ---- 宿主能力回调（定时器），由宿主实现并注入 ---- */
typedef struct {
    void (*timerStart)(WORD32 timerMsgId, WORD32 duration);
    void (*timerStop)(WORD32 timerMsgId);
} StepHost;
void stepSetHost(const StepHost *host);
/* ---- 引擎核心 ---- */
StepRet stepRun(Instance *inst, WORD32 msgId, void *msg, WORD32 len);
StepRet stepResume(Instance *inst, WORD32 msgId, void *msg, WORD32 len);
#ifdef __cplusplus
}
#endif
