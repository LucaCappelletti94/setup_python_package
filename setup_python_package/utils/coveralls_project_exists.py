from .url_exists import url_exists

def coveralls_project_exists(account: str, package: str)->bool:
    """Return boolean representing if given coveralls project exists."""
    return url_exists(
        "https://coveralls.io/github/{account}/{package}".format(
            account=account,
            package=package
        )
    )