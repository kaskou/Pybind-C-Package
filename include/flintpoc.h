#pragma once

class FlintPoc {
public:
    FlintPoc(int value);
    int getValue() const;
    void setValue(int value);

private:
    int value_;
};
