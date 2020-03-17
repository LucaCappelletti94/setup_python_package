from .repository_owner_is_python_package_owner import repository_owner_is_python_package_owner
from .python_package_exists import python_package_exists


def is_available_python_package_name(package: str) -> bool:
    """Return boolean representing if given python package name is available."""
    try:
        return not python_package_exists(package) or repository_owner_is_python_package_owner(package)
    except ValueError as e:
        print(e)

    return False
