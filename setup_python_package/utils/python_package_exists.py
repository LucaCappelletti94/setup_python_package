from .get_python_package_informations import get_python_package_informations
import json


def python_package_exists(package: str) -> bool:
    """Return a boolean representing if given package is online on pypi.

    Parameters
    -----------------------
    package: str,
        The package name.

    Returns
    -----------------------
    Boolean representing if given package is online.
    """
    try:
        get_python_package_informations(package)
        return True
    except json.decoder.JSONDecodeError:
        return False
