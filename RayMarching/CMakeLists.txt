cmake_minimum_required(VERSION 3.22)
project(RayMarching)

set(CMAKE_CXX_STANDARD 20)

add_executable(RayMarching objects.cpp raymarching.cpp)

find_package(SFML 2.5 COMPONENTS system graphics audio REQUIRED)
target_link_libraries(RayMarching sfml-system sfml-graphics sfml-audio)
