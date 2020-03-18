from setup_python_package.builders import build_gitignore
from .utils import clone_test_repo, delete_test_repo


def test_build_gitignore():
    clone_test_repo()
    build_gitignore()
    delete_test_repo()