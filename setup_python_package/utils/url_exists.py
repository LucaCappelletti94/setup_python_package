import requests


def url_exists(url: str, max_redirect: int = 1) -> bool:
    """Return boolean representing if given url is reacheable.

    Parameters
    ----------------------------
    url:str,
        The url to check for.

    Returns
    ----------------------------
    Boolean representing if given url is reacheable.
    """
    session = requests.Session()
    session.max_redirects = max_redirect
    try:
        return session.get(url).status_code == 200
    except (requests.TooManyRedirects, requests.exceptions.ConnectionError):
        return False
