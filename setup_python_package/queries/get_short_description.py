from ..utils import get_default_short_package_description
from userinput import userinput


def get_short_description() -> str:
    return userinput(
        name="short description",
        label="Enter a short description for the python package.",
        default=get_default_short_package_description(),
        validator="non_empty",
        sanitizer=[
            "strip"
        ],
        auto_clear=True,
        cache=False
    )
