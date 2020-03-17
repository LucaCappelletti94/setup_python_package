from setup_python_package.utils import coveralls_project_exists


def test_coveralls_project_exists():
    assert coveralls_project_exists()