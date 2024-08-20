cmake_minimum_required(VERSION 3.12)
project(flintwheelpoc)

set(CMAKE_CXX_STANDARD 14)

# Find pybind11 package
find_package(pybind11 REQUIRED)

# Include directories
include_directories(${CMAKE_SOURCE_DIR}/include)

# Create the Python module
pybind11_add_module(flintwheelpoc_module src/flintpoc.cpp src/bindings.cpp)
