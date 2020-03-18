from setup_python_package import setup_python_package
from .utils import clone_test_repo, delete_test_repo
from environments_utils import is_stdout_enabled


def test_manual_setup_python_package():
    if is_stdout_enabled():
        clone_test_repo()
        setup_python_package()
        delete_test_repo()