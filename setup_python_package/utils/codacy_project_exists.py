from .url_exists import url_exists

def codacy_project_exists(account: str, package: str)->bool:
    """Return boolean representing if given codacy project exists."""
    return url_exists(
        "https://app.codacy.com/project/{account}/{package}/dashboard".format(
            account=account,
            package=package
        )
    )