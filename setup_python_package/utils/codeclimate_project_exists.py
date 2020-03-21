from .url_exists import url_exists
from .load_repository import load_repository_name, load_repository_organization


def codeclimate_project_exists() -> bool:
    """Return boolean representing if given codeclimate project exists."""
    return url_exists(
        "https://codeclimate.com/github/{organization}/{repository}".format(
            organization=load_repository_organization(),
            repository=load_repository_name()
        )
    )
