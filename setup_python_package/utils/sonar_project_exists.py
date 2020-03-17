import requests
from .load_repository import load_repository_name, load_repository_author_name


def sonar_project_exists() -> bool:
    """Return boolean representing if given sonar project exists."""
    return "project not found" not in requests.get(
        "https://sonarcloud.io/api/project_badges/measure?project={account}_{repository}&metric=coverage".format(
            account=load_repository_author_name(),
            repository=load_repository_name()
        )
    ).text.lower()
