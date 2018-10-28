"""
@description: Example package setup.py

setup.py is build script for setuptools
"""
import setuptools

if __name__ == "__main__":
    # Get long description from README.md
    with open("README.md", "r") as f:
        long_description = f.read()

    # Basic setuptools call
    setuptools.setup(
        name="example_pkg", # name of package; AZ az 09 -_
        version="0.0.1",    # implementation-dependent; for official: https://www.python.org/dev/peps/pep-0440/
        author="dweng",
        author_email="darrel.weng@gmail.com",
        description="Example Python package",
        # Shown on package detail of Python Package Index; common pattern to use README.md
        long_description=long_description,
        # Homepage/url of project (source)
        url="https://github.com/xialu000/python-scratch/examle_pkg",
        # List of all Python import packages that should be included with
        #   distribution package.  Let setuptools auto-discover them here.
        packages=setuptools.find_packages(),
        # Metadata for pip/index
        #   Complete list of classifiers: https://pypi.org/classifiers
        classifiers=[
            "Development Status :: 3 - Alpha",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
            "Programming Lanugage :: Python :: 2.7",
            "Programming Language :: Python :: 3.7",
        ]
    )

