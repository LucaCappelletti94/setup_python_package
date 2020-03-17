import os
from ..utils import load_configuration

def build_version_test(package: str):
    with open("{}/models/version_test".format(os.path.dirname(os.path.abspath(__file__))), "r") as source:
        with open("{}/test_version.py".format(load_configuration()["tests_directory"]), "w") as sink:
            sink.write(source.read().format(package=package))
