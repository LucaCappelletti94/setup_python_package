def normalize_package_name_for_pypi(package: str) -> str:
    """Normalize given string into a valid python package for pypi.

    Parameters
    ------------------------
    package: str,
        The name of the package.

    Raises
    ------------------------
    ValueError,
        When the name of the package contains spaces.

    Returns
    ------------------------
    Sanitized package name.
    """
    if any(target in package for target in (" ",)):
        raise ValueError("Given package name is not normalizable.")

    return package.lower().replace("_", "-")


def normalize_package_name_for_code(package: str) -> str:
    """Normalize given string into a valid python package for code usage.

    Parameters
    ------------------------
    package: str,
        The name of the package.

    Raises
    ------------------------
    ValueError,
        When the name of the package contains spaces.

    Returns
    ------------------------
    Sanitized package name.
    """
    if any(target in package for target in (" ",)):
        raise ValueError("Given package name is not normalizable.")

    return package.lower().replace("-", "_")
