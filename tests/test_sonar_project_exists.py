from setup_python_package.utils import sonar_project_exists


def test_sonar_project_exists():
    assert sonar_project_exists("LucaCappelletti94_setup_python_package")
