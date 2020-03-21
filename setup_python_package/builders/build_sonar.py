import os
from ..utils import load_configuration, load_repository_organization, load_repository_url


def build_sonar(**kwargs):
    with open("{}/models/sonar".format(os.path.dirname(os.path.abspath(__file__))), "r") as source:
        with open("sonar-project.properties", "w") as sink:
            sink.write(source.read().format(
                **kwargs,
                repository_url=load_repository_url(),
                organization=load_repository_organization(),
                tests_directory=load_configuration()["tests_directory"]
            ))