import os
from ..utils import load_configuration, load_repository_author_name, load_repository_url


def build_sonar(package: str, version: str):
    with open("{}/models/sonar".format(os.path.dirname(os.path.abspath(__file__))), "r") as source:
        with open("sonar-project.properties", "w") as sink:
            sink.write(source.read().format(
                package=package,
                account=load_repository_author_name(),
                account_lower=load_repository_author_name().lower(),
                url=load_repository_url(),
                version=version,
                tests_directory=load_configuration()["tests_directory"]
            ))