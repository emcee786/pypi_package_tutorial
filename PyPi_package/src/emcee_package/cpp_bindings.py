import ctypes
import os

lib_path = os.path.join(os.path.dirname(__file__), "libcppstring.so")
_cpp = ctypes.CDLL(lib_path)

def cpp_laters():
    return _cpp.cpp_laters()


def cpp_hey():
    return _cpp.cpp_hey()

