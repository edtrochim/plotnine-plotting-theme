from setuptools import setup, find_packages

setup(
    name="colab-plotting-theme",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="Custom plotting theme for Google Colab with Open Sans font",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/colab-plotting-theme",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[
        "plotnine>=0.10.0",
        "matplotlib>=3.5.0",
    ],
)
