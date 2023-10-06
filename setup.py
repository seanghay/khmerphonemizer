import numpy as np
from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize(
        "khmerphonemizer/g2p_phonetisaurus.pyx",
        include_path=[np.get_include()],
    ),
)
