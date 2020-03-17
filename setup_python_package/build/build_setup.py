import re
import os
import json
from .build_manifest import build_manifest
from ..utils import load_configuration

def build_setup(package: str, short_description: str, url: str, author: str, email: str):
    build_manifest()
    path = "setup.py"
    test_dependencies = load_configuration()["tests_dependencies"]
    install_dependencies = []
    if os.path.exists(path):
        with open(path, "r") as f:
            content = f.read()
        try:
            if "test_deps" in content:
                test_dependencies = list(set(test_dependencies + [
                    key.strip("\"' \n") for key in re.compile(r"test_deps\s*=\s*\[([\s\S]+?)\]").findall(content)[0].split(",")
                ]))
        except Exception:
            pass
        try:
            if "install_requires" in content:
                install_dependencies = list(set(install_dependencies+[
                    key.strip("\"' \n") for key in re.compile(r"install_requires\s*=\s*\[([\s\S]+?)\]").findall(content)[0].split(",")
                ]))
        except Exception:
            pass

        path = "suggested_setup.py"
        print("I am not touching your setup.py, you'll need to update it yourself.")
        print("I have generated a suggested one called {}".format(path))

    with open("{}/models/setup".format(os.path.dirname(os.path.abspath(__file__))), "r") as source:
        with open(path, "w") as sink:
            sink.write(source.read().format(
                package=package,
                short_description=short_description,
                url=url,
                author=author,
                email=email,
                install_dependencies=json.dumps(
                    install_dependencies, indent=4),
                test_dependencies=json.dumps(test_dependencies, indent=4)
            ))