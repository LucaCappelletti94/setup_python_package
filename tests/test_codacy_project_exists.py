from setup_python_package.utils import codacy_project_exists

def test_codacy_project_exists():
    assert codacy_project_exists()