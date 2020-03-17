from .load_repository import load_repository_name
from .normalize_package_name import normalize_package_name_for_code


def get_default_package_name()->str:
    """Return default package name based on repo name."""
    return normalize_package_name_for_code(load_repository_name())
