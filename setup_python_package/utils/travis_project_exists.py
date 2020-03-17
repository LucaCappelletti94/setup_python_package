import requests


def travis_project_exists(account: str, package: str) -> bool:
    """Return boolean representing if given travis project exists."""
    return "unknown" not in requests.get(
        "https://api.travis-ci.org/{account}/{package}.svg".format(
            account=account,
            package=package
        )
    ).text
