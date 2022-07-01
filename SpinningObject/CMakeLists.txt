cmake_minimum_required(VERSION 3.22)
project(SpinningObject)

find_package(OpenGL REQUIRED)

set(CMAKE_CXX_STANDARD 23)
set(OpenGlLinkers -lglut -lGLU -lGL -lGLEW -lglfw)

add_executable(SpinningObject main.cpp)
add_executable(SpinningObjectTest test.cpp)
target_link_libraries(SpinningObject ${OpenGlLinkers})
