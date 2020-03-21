from .url_exists import url_exists
from .load_repository import load_repository_name, load_repository_organization


def coveralls_project_exists() -> bool:
    """Return boolean representing if given coveralls project exists."""
    return url_exists(
        "https://coveralls.io/github/{organization}/{repository}".format(
            organization=load_repository_organization(),
            repository=load_repository_name()
        )
    )
