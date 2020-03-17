from setup_python_package.queries import get_sonar_code

def test_get_sonar_code(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda x: "1111111111111111111111111111111111111111")
    get_sonar_code()