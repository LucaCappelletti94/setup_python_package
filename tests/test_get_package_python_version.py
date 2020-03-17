from setup_python_package.queries import get_package_version
from setup_python_package.utils import get_default_package_version


def test_get_package_version(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda x: "\n")
    assert get_package_version() == get_default_package_version()
    monkeypatch.setattr('builtins.input', lambda x: "3.7.0")
    assert get_package_version() == "3.7.0"