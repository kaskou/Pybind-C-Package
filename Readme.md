### Building and Running the C++ Python Extension Module

This document provides instructions for building and running a C++ Python extension module using a `setup.py` file and a bash script. It also includes guidance for running a sample Python test script.

---

#### 1. **Project Structure**

Ensure your project is organized as follows:

```
/project
    /include
        flintpoc.h
    /src
        flintpoc.cpp
        bindings.cpp
    setup.py
    run.sh
    test.py
    CMakeLists.txt
```

---

#### 2. **Building the Project**

1. **Make the Bash Script Executable**

   Before running the build script, ensure it has executable permissions. Use the following command:

   ```bash
   chmod +x run.sh
   ```

2. **Run the Build Script**

   Execute the `run.sh` script to configure, build, and compile the Python extension module. In your terminal, navigate to the project directory and run:

   ```bash
   ./run.sh
   ```

   The script performs the following actions:
   - Creates a `build` directory if it doesn't exist.
   - Configures the project with `cmake`.
   - Compiles the project with `make` (if applicable).
   - Creates the build directory for the Python extension module.
   - Builds the Python extension module using `setup.py`.

---

#### 3. **Running the Sample Test Script**

After successfully building the module, you can test it using a Python script.

1. **Create the Test Script**

   Create a file named `test.py` in the project directory with the following content:

   ```python
    import flintwheelpoc_module
    
    obj = flintwheelpoc_module.FlintPoc(10)
    print(obj.getValue())  # Output: 10
    
    obj.setValue(20)
    print(obj.getValue())  # Output: 20
   ```

2. **Run the Test Script**

   Use Python to execute the test script. In your terminal, run:

   ```bash
   python test.py
   ```

   This script imports the `flintwheelpoc_module` module and verifies the functionality of the `FlintPoc` class by calling its methods.

---

# 4. **Additional Notes**
Test Version 1
