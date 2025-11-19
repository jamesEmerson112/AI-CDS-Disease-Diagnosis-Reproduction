from setuptools import setup, Extension
from Cython.Build import cythonize
import numpy

# Define the extension module
extensions = [
    Extension(
        "util_cy",
        ["util_cy.c"],
        include_dirs=[numpy.get_include()],
        extra_compile_args=['-O3']
    )
]

setup(
    name="util_cy",
    ext_modules=extensions,
    zip_safe=False,
)
