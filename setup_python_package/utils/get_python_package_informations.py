from .format_pypi_api_url import format_pypi_api_url
import requests
from typing import Dict


def get_python_package_informations(package: str) -> Dict:
    """Return python package informations."""
    url = format_pypi_api_url(package)
    return requests.get(url, headers={'Accept': 'application/json'}).json()
