from setuptools import setup, Extension
import pybind11
import os
import sys

# Get the path to pybind11
def get_pybind11_include():
    import pybind11
    return pybind11.get_include()

# Define the extension module
ext_modules = [
    Extension(
        'flintwheelpoc_module',
        sources=['src/bindings.cpp', 'src/flintpoc.cpp'],
        include_dirs=[
            'include',            # Path to your header files
            get_pybind11_include(),  # Path to pybind11 headers
            # get_pybind11_include(True)  # Path to pybind11 headers for C++11
        ],
        language='c++'
    ),
]

# Setup configuration
setup(
    name='flintwheelpoc_module',
    version='0.1',
    author='Your Name',
    author_email='your.email@example.com',
    description='A Python module that wraps a C++ class using Pybind11',
    ext_modules=ext_modules,
    zip_safe=False,
)
