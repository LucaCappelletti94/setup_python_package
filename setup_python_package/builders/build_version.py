import os

def build_version(package: str, version:str):
    """Write version file for the package."""
    os.makedirs(package, exist_ok=True)
    with open("{}/models/version".format(os.path.dirname(os.path.abspath(__file__))), "r") as source:
        with open("{package}/__version__.py".format(package=package), "w") as sink:
            sink.write(source.read().format(
                version=version,
                package=package
            ))
