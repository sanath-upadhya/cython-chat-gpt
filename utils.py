CYTHON_CODE_REQUEST_DOC_STRING = "Write a cython code for the following description and begin the code with %%cython: "
CYTHON_CODE_REQUEST_PYTHON_STRING = "Write a cython code for the following python code and begin the code with %%cython:"
CYTHON_CODE_REQUEST_PYTHON_DOC_STRING = "and the python code for the same is:"

CYTHON_SETUP_FILE = ["from distutils.core import setup", 
                     "from Cython.Build import cythonize", 
                     "from distutils.extension import Extension",
                     "setup(ext_modules = cythonize('tmp/custom_cython.pyx'))"]

CYTHON_COMPILE_EXEC_COMMAND = ["python3","tmp/setup.py","build_ext","--inplace"]


def write_to_file(content):
    f = open("output.txt", "a")
    f.write(content + '\n')
    f.close()
