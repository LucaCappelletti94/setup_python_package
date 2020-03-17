from .url_exists import url_exists
from .load_repository import load_repository_name, load_repository_author_name


def codacy_project_exists() -> bool:
    """Return boolean representing if given codacy project exists."""
    return url_exists(
        "https://app.codacy.com/project/{account}/{repository}/dashboard".format(
            account=load_repository_author_name(),
            repository=load_repository_name()
        )
    )
