from userinput import userinput
from ..utils import load_repository_author_name


def get_package_author_name() -> str:
    """Return the package author name to be used."""
    return userinput(
        name="python_package_author_name",
        label="Enter the python package author name to use.",
        default=load_repository_author_name(),
        validator="non_empty",
        sanitizer=[
            "strip"
        ],
        auto_clear=True,
        cache=False
    )
