from setup_python_package.utils import codeclimate_project_exists

def test_codeclimate_project_exists():
    assert codeclimate_project_exists("LucaCappelletti94", "setup_python_package")
    assert not codeclimate_project_exists("LucaCappelletti94", "kwegfkejhfgewjfjwefgipefjb")