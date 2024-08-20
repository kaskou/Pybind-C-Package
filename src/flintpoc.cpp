#include "flintpoc.h"

FlintPoc::FlintPoc(int value) : value_(value) {}

int FlintPoc::getValue() const {
    return value_;
}

void FlintPoc::setValue(int value) {
    value_ = value;
}
