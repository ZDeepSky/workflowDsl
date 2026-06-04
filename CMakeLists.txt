cmake_minimum_required(VERSION 3.16)
project(workflowDsl C CXX)

set(CMAKE_C_STANDARD 11)
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# --- library: dispatch sources ---
add_library(workflow_dsl STATIC
    dispatch/source/step_engine.c
    dispatch/source/step_impl.cc
    dispatch/source/workflows_gen.c
)
target_include_directories(workflow_dsl PUBLIC
    ${CMAKE_SOURCE_DIR}/dispatch/include
)

# --- Google Test ---
include(FetchContent)
FetchContent_Declare(
    googletest
    URL https://github.com/google/googletest/archive/refs/tags/v1.14.0.zip
)
set(gtest_force_shared_crt ON CACHE BOOL "" FORCE)
FetchContent_MakeAvailable(googletest)

enable_testing()

# --- step_engine_ut ---
add_executable(step_engine_ut test/code/ut/step_engine_ut.cpp)
target_include_directories(step_engine_ut PRIVATE
    ${CMAKE_SOURCE_DIR}/test
    ${CMAKE_SOURCE_DIR}/dispatch/include
)
target_link_libraries(step_engine_ut PRIVATE workflow_dsl GTest::gtest_main)
add_test(NAME step_engine_ut COMMAND step_engine_ut)
