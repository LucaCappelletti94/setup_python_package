from setup_python_package.queries import get_package_name
from setup_python_package.utils import is_available_python_package_name


def test_get_package_name(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda x: "\n")
    assert get_package_name() == "setup_python_package"
    monkeypatch.setattr('builtins.input', lambda x: "new_package_name_never_used_before")
    assert get_package_name() == "new_package_name_never_used_before"
    monkeypatch.setattr('builtins.input', lambda x: "new-package-name-never-used-before")
    assert get_package_name() == "new_package_name_never_used_before"
    assert not is_available_python_package_name("invalid python package name")
