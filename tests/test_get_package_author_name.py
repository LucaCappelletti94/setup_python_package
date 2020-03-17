from setup_python_package.queries import get_package_author_name


def test_get_package_author_name(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda x: "\n")
    assert get_package_author_name() == "Luca Cappelletti"
    monkeypatch.setattr('builtins.input', lambda x: "Pinco Pallino")
    assert get_package_author_name() == "Pinco Pallino"
