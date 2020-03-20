from userinput import userinput
from ..utils import get_default_package_version


def get_package_version() -> str:
    """Return the package version to be used."""
    return userinput(
        name="_version",
        label="Enter the package version to use",
        default=get_default_package_version(),
        validator="version_code",
        cache=False,
        maximum_attempts=50
    )
