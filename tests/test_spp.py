from setup_python_package import setup_python_package

def monkeypatch_input(*args, **kwargs):
    return "\n"

def test_spp(monkeypatch):
    monkeypatch.setattr('builtins.input', monkeypatch_input)
    setup_python_package()