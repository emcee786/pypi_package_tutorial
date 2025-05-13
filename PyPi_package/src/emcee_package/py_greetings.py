from .cpp_bindings import cpp_laters 
# Python Functions
def hello():
    print("Hello from Emcee!")

def bye():
    print("Bye from Emcee!")


# From CPP file
def laters():
    cpp_laters()