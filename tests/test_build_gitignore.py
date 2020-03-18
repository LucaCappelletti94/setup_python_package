from setup_python_package.builders import build_gitignore, build_init, build_tests
from setup_python_package.builders.build_manifest import build_manifest
from .utils import clone_test_repo, delete_test_repo


def test_build_gitignore():
    clone_test_repo()
    build_gitignore()
    package = "setup_python_package_test_reporitory"
    build_init(package)
    build_manifest()
    build_tests(package)
    assert open(".gitignore", "r").read() == open("../expected/.gitignore", "r").read()
    delete_test_repo()