from userinput import userinput
from ..utils import get_default_package_name, is_available_python_package_name, normalize_package_name_for_code


def get_package_name() -> str:
    """Return the package name to be used."""
    return userinput(
        name="python_package_name",
        label="Enter the python package name to use. It must follow PEP8 rules for package names.",
        default=get_default_package_name(),
        validator=is_available_python_package_name,
        sanitizer=normalize_package_name_for_code,
        cache=False
    )
