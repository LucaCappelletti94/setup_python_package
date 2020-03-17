import os
from ..utils import load_configuration


def build_sonar(package: str, account: str, url: str, version: str):
    with open("{}/models/sonar".format(os.path.dirname(os.path.abspath(__file__))), "r") as source:
        with open("sonar-project.properties", "w") as sink:
            sink.write(source.read().format(
                package=package,
                account=account,
                account_lower=account.lower(),
                url=url,
                version=version,
                tests_directory=load_configuration()["tests_directory"]
            ))