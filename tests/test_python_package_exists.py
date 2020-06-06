from setup_python_package.utils.python_package_exists import python_package_exists

def test_python_package_exists():
    assert python_package_exists("numpy")
    assert not python_package_exists("asdfjklljuiwehfiuwhefgkwfgkewfgwehjfgkjwegfh")
    assert not python_package_exists("cdesf2")