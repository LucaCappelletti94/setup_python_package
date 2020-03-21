import os
from ..queries import get_long_description
from ..badges import load_badges
from ..utils import load_repository_organization, load_repository_name, normalize_package_name_for_pypi


def build_readme(
    package: str,
    short_description: str,
    project_key
):
    with open("{}/models/readme".format(os.path.dirname(os.path.abspath(__file__))), "r") as source:
        with open("README.rst", "w") as sink:
            sink.write(source.read().format(
                package=package,
                pypi_package=normalize_package_name_for_pypi(package),
                organization=load_repository_organization(),
                repository=load_repository_name(),
                short_description=short_description,
                long_description=get_long_description(),
                project_key=project_key,
                **load_badges()
            ))
    if os.path.exists("README.md"):
        os.remove("README.md")