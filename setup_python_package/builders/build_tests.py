import os
from .build_version_test import build_version_test
from .build_init import build_init
from ..utils import load_configuration

def build_tests(package: str):
    """Create minimal test directory."""
    directory = load_configuration()["tests_directory"]
    os.makedirs(directory, exist_ok=True)
    build_init(directory)
    build_version_test(package)
