from userinput import userinput
from ..utils import get_default_python_version


def get_python_version() -> str:
    """Return the python version to be used."""
    return userinput(
        name="python_version",
        label="Enter the python version to use.",
        default=get_default_python_version(),
        validator="version_code",
        auto_clear=True,
        cache=False,
        maximum_attempts=50
    )
