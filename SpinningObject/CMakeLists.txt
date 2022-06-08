cmake_minimum_required(VERSION 3.22)
project(SpinningObject)

find_package(OpenGL REQUIRED)

set(CMAKE_CXX_STANDARD 20)
set(OpenGlLinkers -lglut -lGLU -lGL)

add_executable(SpinningObject main.cpp)
target_link_libraries(SpinningObject ${OpenGlLinkers})
