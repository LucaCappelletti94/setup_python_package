from .url_exists import url_exists

def codeclimate_project_exists(account: str, package: str)->bool:
    """Return boolean representing if given codeclimate project exists."""
    return url_exists(
        "https://codeclimate.com/github/{account}/{package}".format(
            account=account,
            package=package
        )
    )