import os
import re
import sys
# To use a consistent encoding
from codecs import open
from os import path

from setuptools import find_packages, setup

here = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()


def read(*parts):
    with open(os.path.join(here, *parts), 'r') as fp:
        return fp.read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(
        r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


__version__ = find_version("setup_python_package", "__version__.py")

test_deps = ['pytest', 'pytest-cov', 'coveralls', 'validate_version_code']

extras = {
    'test': test_deps,
}

setup(
    name='setup_python_package',
    version=__version__,
    description="A python package that helps you create a python package.",
    long_description=long_description,
    url="https://github.com/LucaCappelletti94/setup_python_package",
    author="Luca Cappelletti",
    author_email="cappelletti.luca94@gmail.com",
    # Choose your license
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3'
    ],
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    tests_require=test_deps,
    install_requires=[
        "gitpython", "requests", "validate_email", "validate_version_code", "pathlib", "validators", "webbrowser"
    ],
    extras_require=extras,
)
