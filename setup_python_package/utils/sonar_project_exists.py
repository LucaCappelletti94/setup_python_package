import requests


def sonar_project_exists(account: str, package: str) -> bool:
    """Return boolean representing if given sonar project exists."""
    return "project not found" not in requests.get(
        "https://sonarcloud.io/api/project_badges/measure?project={account}_{package}&metric=coverage".format(
            account=account,
            package=package
        )
    ).text.lower()
