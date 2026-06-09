cmake_minimum_required(VERSION 3.16)
project(workflowDsl_test CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

set(WORKFLOW_DSL_ROOT ${CMAKE_CURRENT_SOURCE_DIR}/..)
add_subdirectory(${WORKFLOW_DSL_ROOT} ${CMAKE_BINARY_DIR}/lib)

include(FetchContent)
FetchContent_Declare(
    googletest
    URL https://github.com/google/googletest/archive/refs/tags/v1.14.0.zip
)
set(gtest_force_shared_crt ON CACHE BOOL "" FORCE)
FetchContent_MakeAvailable(googletest)

enable_testing()

add_executable(step_engine_ut code/ut/step_engine_ut.cpp)
target_include_directories(step_engine_ut PRIVATE
    ${CMAKE_CURRENT_SOURCE_DIR}
    ${WORKFLOW_DSL_ROOT}/dispatch/pub_inlcude
)
target_link_libraries(step_engine_ut PRIVATE workflow_dsl GTest::gtest_main)
add_test(NAME step_engine_ut COMMAND step_engine_ut)
