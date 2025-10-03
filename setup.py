from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="colab-plotting-theme",
    version="0.1.0",
    author="Erin Trochim",
    description="Custom plotting theme for Google Colab with Open Sans font",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/edtrochim/plotnine-plotting-theme",
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",  # Fixed to match LICENSE
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[
        "plotnine>=0.10.0",
        "matplotlib>=3.5.0",
    ],
)
