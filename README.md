# emcee_package

**Version**: 0.3.1  
**Author**: Emcee  
**Description**: A Python package with C++ bindings, featuring Python and native extensions compiled as `.so` files.

> This package was built as an experiment to learn about publishing Python packages and integrating C++ functions and bindings into Python.  
> Initial PyPI setup followed the [Pixegami tutorial](https://www.youtube.com/watch?v=Kz6IlDCyOUYcd).

---

## 📦 Installation

Make sure you have [Hatch](https://hatch.pypa.io/) installed:

```bash
pip install hatch

Build the project:

hatch build

Install the package:

pip install dist/emcee_package-0.3.1-py3-none-any.whl

    🔁 Replace the version number in the .whl filename if you've updated it.

🧪 Running the Check Script

To test the package locally without installing it:

PYTHONPATH=src python check.py

    This works because the package uses a src/ layout, and the source directory must be discoverable by Python.

Once the package is installed via pip, you can also run:

python check.py

🔧 Project Layout

.
├── check.py                  # Sample script to test package functions
├── pyproject.toml            # Hatchling build configuration
├── README.md                
├── src/
│   └── emcee_package/
│       ├── __init__.py
│       ├── cpp_bindings.py   # Python bindings to compiled .so
│       ├── cpp_greetings.cpp # C++ source file (for reference)
│       ├── libcppstring.so   # Compiled C++ shared object
│       ├── py_greetings.py   # Python-only greeting functions

🛠 CLI Commands

After installing the package, the following CLI commands will be available:

emcee-bye     # runs emcee_package.py_greetings:bye()
emcee-laters  # runs emcee_package.py_greetings:laters()

These are defined in the [project.scripts] section of pyproject.toml.
🔨 Build From Source

To clean old builds:

rm -rf dist build *.egg-info

Then rebuild:

hatch build

To reinstall:

pip install dist/emcee_package-0.3.1-py3-none-any.whl --force-reinstall

📝 Requirements

    Python 3.7 or higher

    Hatch to manage builds

    A precompiled C++ shared object (libcppstring.so) placed in src/emcee_package/

    This project assumes the .so file is already compiled and placed correctly. C++ build automation (e.g., via setuptools, CMake, or build_ext) is not included.

🧪 Development Notes

For development convenience, you can use:

hatch shell
python check.py

Or manually set your environment:

PYTHONPATH=src python check.py


