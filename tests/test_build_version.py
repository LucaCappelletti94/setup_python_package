from setup_python_package.builders import build_version
from setup_python_package.queries import get_package_name
from .utils import clone_test_repo, delete_test_repo


def test_build_version(monkeypatch):
    clone_test_repo()
    monkeypatch.setattr('builtins.input', lambda x: "\n")
    package = get_package_name()
    build_version(package)
    #assert open(f"{package}/__version__.py", "r").read() == open(f"../expected/{package}/__version__.py", "r").read()
    delete_test_repo()