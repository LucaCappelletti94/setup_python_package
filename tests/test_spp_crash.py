from setup_python_package import setup_python_package
from .utils import clone_test_repo, delete_test_repo
import os


def crash(label):
    raise KeyboardInterrupt()

def test_setup_python_package(monkeypatch):
    clone_test_repo()
    files1 = len(os.listdir())
    monkeypatch.setattr('builtins.input', crash)
    setup_python_package()
    files2 = len(os.listdir())
    delete_test_repo()
    assert files2 == files1
