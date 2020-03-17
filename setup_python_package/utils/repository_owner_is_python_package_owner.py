from .load_repository import load_repository_url
from .get_python_package_informations import get_python_package_informations


def repository_owner_is_python_package_owner(package: str) -> bool:
    """Return boolean representing if repository URL is package url."""
    return get_python_package_informations(package)["info"]["home_page"] == load_repository_url()
