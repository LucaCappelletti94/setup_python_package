import os
import re
import sys
# To use a consistent encoding
from codecs import open as copen
from os import path
from validate_version_code import extract_version_code
from setuptools import find_packages, setup

here = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file
with copen(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

__version__ = extract_version_code("setup_python_package")

test_deps = ['pytest', 'pytest-cov', 'coveralls', 'validate_version_code', 'codacy-coverage']

extras = {
    'test': test_deps,
}

setup(
    name='setup_python_package',
    version=__version__,
    description="A python package that helps you create a python package.

The script will guide you step by step in creating the python package and integrating it with sonarcloud, travis and coveralls.
",
    long_description=long_description,
    url="https://github.com/LucaCappelletti94/setup_python_package",
    author="Luca Cappelletti",
    author_email="cappelletti.luca94@gmail.com",
    # Choose your license
    license='MIT',
    include_package_data=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3'
    ],
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    tests_require=test_deps,
    install_requires=[
        # Add here the package dependencies
    ],
    extras_require=extras,
)