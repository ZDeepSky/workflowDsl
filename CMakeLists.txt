cmake_minimum_required(VERSION 3.16)
project(workflowDsl C CXX)

set(CMAKE_C_STANDARD 11)
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

set(WORKFLOW_DSL_ROOT ${CMAKE_CURRENT_SOURCE_DIR})
set(WORKFLOW_DSL_PUB_INCLUDE ${WORKFLOW_DSL_ROOT}/dispatch/pub_inlcude)
set(WORKFLOW_DSL_OUTPUT_DIR ${WORKFLOW_DSL_ROOT}/output)
set(WORKFLOW_DSL_LIB_DIR ${WORKFLOW_DSL_OUTPUT_DIR}/lib)
set(WORKFLOW_DSL_INCLUDE_DIR ${WORKFLOW_DSL_OUTPUT_DIR}/include)



file(GLOB WORKFLOW_DSL_SOURCES
    ${WORKFLOW_DSL_ROOT}/dispatch/source/*.c
    ${WORKFLOW_DSL_ROOT}/dispatch/source/*.cc
)

add_library(workflow_dsl STATIC ${WORKFLOW_DSL_SOURCES})
target_include_directories(workflow_dsl PUBLIC
    ${WORKFLOW_DSL_PUB_INCLUDE}
)

add_custom_command(TARGET workflow_dsl POST_BUILD
    COMMAND ${CMAKE_COMMAND} -E make_directory ${WORKFLOW_DSL_LIB_DIR}
    COMMAND ${CMAKE_COMMAND} -E make_directory ${WORKFLOW_DSL_INCLUDE_DIR}
    COMMAND ${CMAKE_COMMAND} -E copy $<TARGET_FILE:workflow_dsl> ${WORKFLOW_DSL_LIB_DIR}/
    COMMAND ${CMAKE_COMMAND} -E copy_directory ${WORKFLOW_DSL_PUB_INCLUDE} ${WORKFLOW_DSL_INCLUDE_DIR}
    COMMENT "Copy libworkflow_dsl.a and public headers to output/"
)
