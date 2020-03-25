from .repository_owner_is_python_package_owner import repository_owner_is_python_package_owner
from .normalize_package_name import normalize_package_name_for_pypi
from .python_package_exists import python_package_exists


def is_available_python_package_name(package: str) -> bool:
    """Return boolean representing if given python package name is available."""
    try:
        normalize_package_name_for_pypi(package)
    except Exception:
        print("Given package name {} is not a valid package name.".format(
            package
        ))
        return False

    if not python_package_exists(package) or repository_owner_is_python_package_owner(package):
        return True
    print("Given package name {} is already used and this repository does not match with the package repository.".format(
        package
    ))
    return False