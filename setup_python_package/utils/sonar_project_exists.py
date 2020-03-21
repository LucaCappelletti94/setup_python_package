import requests


def sonar_project_exists(project_key: str) -> bool:
    """Return boolean representing if given sonar project exists."""
    return "project not found" not in requests.get(
        "https://sonarcloud.io/api/project_badges/measure?project={project_key}&metric=coverage".format(
            project_key=project_key
        )
    ).text.lower()
