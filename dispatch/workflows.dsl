// Sample workflow DSL for code generation demos and integration tests.

@action init = step_init
@action select_handler = step_select_handler
@action respond = step_respond
@action cleanup = step_cleanup
@action process_data = step_process_data
@condition isComplete = cond_isComplete

workflow SimpleFlow
{
    action  init
    action  select_handler
    recv    process_data
    action  respond
    while not isComplete:
        goto process_data
    final:
        action  cleanup
}

action ACTION_SIMPLE_A = SimpleFlow
action ACTION_SIMPLE_B = SimpleFlow
