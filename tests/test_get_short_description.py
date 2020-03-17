from setup_python_package.queries import get_short_description
from setup_python_package.utils import get_default_short_package_description


def test_get_short_description(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda x: "\n")
    assert get_short_description() == get_default_short_package_description()
    monkeypatch.setattr('builtins.input', lambda x: "new_package_name_never_used_before")
    assert get_short_description() == "new_package_name_never_used_before"
