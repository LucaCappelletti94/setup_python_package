from .normalize_package_name import normalize_package_name_for_pypi


def format_pypi_api_url(package: str) -> str:
    """Return pypi url for given package."""
    return "https://pypi.org/pypi/{}/json".format(
        normalize_package_name_for_pypi(package)
    )
