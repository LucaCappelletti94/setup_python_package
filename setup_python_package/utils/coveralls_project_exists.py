from .url_exists import url_exists
from .load_repository import load_repository_name, load_repository_author_name


def coveralls_project_exists() -> bool:
    """Return boolean representing if given coveralls project exists."""
    return url_exists(
        "https://coveralls.io/github/{account}/{repository}".format(
            account=load_repository_author_name(),
            repository=load_repository_name()
        )
    )
