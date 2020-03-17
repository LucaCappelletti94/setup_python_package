from setup_python_package.queries import get_long_description
from setup_python_package.utils import get_default_long_package_description


def test_get_long_description(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda x: "\n")
    assert get_long_description() == get_default_long_package_description()
    monkeypatch.setattr('builtins.input', lambda x: "new_package_name_never_used_before")
    assert get_long_description() == "new_package_name_never_used_before"
