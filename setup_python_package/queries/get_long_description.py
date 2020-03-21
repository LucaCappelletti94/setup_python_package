from ..utils import get_default_long_package_description
from userinput import userinput


def get_long_description() -> str:
    return userinput(
        name="long description",
        label="Enter a long description for the python package.",
        default=get_default_long_package_description(),
        validator="non_empty",
        sanitizer=[
            "strip"
        ],
        cache=False
    )
