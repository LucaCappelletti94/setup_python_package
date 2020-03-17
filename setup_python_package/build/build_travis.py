import os
import webbrowser
from userinput import userinput
from ..utils import travis_project_exists
from ..queries import get_python_version


def build_travis(account: str, package: str):
    if not travis_project_exists(account, package):
        print("You still need to create the travis project.")
        input("Press any key to go to travis now.")
        webbrowser.open(
            "https://travis-ci.org/account/repositories", new=2, autoraise=True)
    if not os.path.exists(".travis.yml"):
        with open("{}/models/travis".format(os.path.dirname(os.path.abspath(__file__))), "r") as source:
            with open(".travis.yml", "w") as sink:
                sink.write(source.read().format(
                    package=package,
                    account=account,
                    account_lower=account.lower(),
                    sonar_travis_code=get_travis_code(package, account),
                    python_version=".".join(
                        get_python_version().split(".")[:2])
                ))
    if userinput(
        "Do you want to add code climate?",
        "yes",
        validator="human_bool",
        sanitizer="human_bool"
    ):
        add_code_climate(account, package)
    if user_input(
        "Do you want to add codacy?",
        "yes",
        validator=validate_boolean_answer,
        incipit=""
    ).lower() == "yes":
        add_codacy(account, package)
