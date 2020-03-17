from setup_python_package.utils import travis_project_exists

def test_travis_project_exists():
    assert travis_project_exists()