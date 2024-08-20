#include <pybind11/pybind11.h>
#include "flintpoc.h"

namespace py = pybind11;

PYBIND11_MODULE(flintwheelpoc_module, m) {
    py::class_<FlintPoc>(m, "FlintPoc")
        .def(py::init<int>())
        .def("getValue", &FlintPoc::getValue)
        .def("setValue", &FlintPoc::setValue);
}
