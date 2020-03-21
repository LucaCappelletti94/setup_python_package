from userinput import userinput
from ..utils import load_repository_author_email


def get_package_author_email() -> str:
    """Return the package author mail to be used."""
    return userinput(
        name="python_package_author_email",
        label="Enter the python package author email to use.",
        default=load_repository_author_email(),
        validator="email",
        cache=False
    )
