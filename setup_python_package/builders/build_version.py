import os
from ..queries import get_package_version


def build_version(package: str):
    """Write version file for the package."""
    os.makedirs(package, exist_ok=True)
    with open("{}/models/version".format(os.path.dirname(os.path.abspath(__file__))), "r") as source:
        with open("{package}/__version__.py".format(package=package), "w") as sink:
            sink.write(source.read().format(
                version=get_package_version(),
                package=package
            ))
