from setup_python_package.queries import get_package_author_email


def test_get_package_author_email(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda x: "\n")
    assert get_package_author_email() == "cappelletti.luca94@gmail.com"
    monkeypatch.setattr('builtins.input', lambda x: "pinco@pallino.com")
    assert get_package_author_email() == "pinco@pallino.com"
