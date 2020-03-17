from setup_python_package.queries import get_python_version
from setup_python_package.utils import get_default_python_version


def test_get_python_version(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda x: "\n")
    assert get_python_version() == get_default_python_version()
    monkeypatch.setattr('builtins.input', lambda x: "1.0.1")
    assert get_python_version() == "1.0.1"