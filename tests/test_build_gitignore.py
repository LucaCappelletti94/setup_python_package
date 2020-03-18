from setup_python_package.builders import build_gitignore, build_init
from setup_python_package.builders.build_manifest import build_manifest
from .utils import clone_test_repo, delete_test_repo


def test_build_gitignore():
    clone_test_repo()
    build_gitignore()
    build_init("setup_python_package_test_reporitory")
    build_manifest()
    assert open(".gitignore", "r").read() == open("../expected/.gitignore", "r").read()
    delete_test_repo()