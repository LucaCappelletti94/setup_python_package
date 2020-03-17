from setup_python_package.utils import get_default_package_name

def test_get_default_package_name():
    assert get_default_package_name() == "setup_python_package"