from setuptools import Extension, setup

setup(
    ext_modules=[
        Extension(
            name="khmerphonemizer.g2p_phonetisaurus",
            sources=["khmerphonemizer/g2p_phonetisaurus.pyx"],
        ),
    ],
)