from setup_python_package import setup_python_package
from .utils import clone_test_repo, delete_test_repo
import os
import pytest

def crash1(label):
    raise KeyboardInterrupt()

def crash2(label):
    raise ValueError()

def test_crash1(monkeypatch):
    clone_test_repo()
    files1 = len(os.listdir())
    monkeypatch.setattr('builtins.input', crash1)
    setup_python_package()
    files2 = len(os.listdir())
    delete_test_repo()
    assert files2 == files1


def test_crash2(monkeypatch):
    clone_test_repo()
    files1 = len(os.listdir())
    monkeypatch.setattr('builtins.input', crash2)
    with pytest.raises(ValueError):
        setup_python_package()
    files2 = len(os.listdir())
    delete_test_repo()
    assert files2 == files1
