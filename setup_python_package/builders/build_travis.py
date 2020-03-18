import os
import webbrowser
from userinput import userinput
from ..utils import travis_project_exists, load_repository_author_name
from ..queries import (get_python_version, get_sonar_code, get_codacy_code,
                       get_codacy_badge, get_code_climate_code, get_code_climate_badges)
from ..badges import badge_exists
from ..enablers import enable_travis


def build_travis(package: str):
    enable_travis()
    if not os.path.exists(".travis.yml"):
        with open("{}/models/travis".format(os.path.dirname(os.path.abspath(__file__))), "r") as source:
            with open(".travis.yml", "w") as sink:
                sink.write(source.read().format(
                    package=package,
                    account=load_repository_author_name().lower(),
                    sonar_travis_code=get_sonar_code(),
                    python_version=".".join(
                        get_python_version().split(".")[:2])
                ))
    if  not badge_exists("code_climate") and userinput(
        "add_code_climate",
        label="Do you want to add code climate?",
        default="yes",
        validator="human_bool",
        sanitizer="human_bool"
    ):
        get_code_climate_code()
        get_code_climate_badges()

    if not badge_exists("codacy") and userinput(
        "add_codacy",
        label="Do you want to add codacy?",
        default="yes",
        validator="human_bool",
        sanitizer="human_bool"
    ):
        get_codacy_code()
        get_codacy_badge()
