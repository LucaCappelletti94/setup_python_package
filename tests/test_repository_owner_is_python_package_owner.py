from setup_python_package.utils.repository_owner_is_python_package_owner import repository_owner_is_python_package_owner

def test_repository_owner_is_python_package_owner():
    assert repository_owner_is_python_package_owner("setup-python-package")
    assert not repository_owner_is_python_package_owner("numpy")