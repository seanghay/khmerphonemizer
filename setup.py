import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="khmerphonemizer",
    version="0.0.1",
    description="A Free, Standalone and Open-Source Khmer Grapheme-to-Phonemes.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/seanghay/khmerphonemizer",
    author="Seanghay Yath",
    author_email="seanghay.dev@gmail.com",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Natural Language :: English",
    ],
    python_requires=">=3.8",
    packages=setuptools.find_packages(exclude=["examples"]),
    package_dir={"khmerphonemizer": "khmerphonemizer"},
    package_data={"khmerphonemizer": ["km_phonemizer.npz", "km_lexicon.tsv"]},
    include_package_data=True,
    install_requires=[
        "numpy>=1.19.0,<2.0.0",
        "khmercut",
    ],
)
