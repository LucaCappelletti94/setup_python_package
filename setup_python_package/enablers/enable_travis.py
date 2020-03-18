from ..utils import travis_project_exists
import webbrowser


def enable_travis(automatically_open_browser: bool):
    if not travis_project_exists():
        print("You still need to create the travis project.")
        if automatically_open_browser:
            input("Press any key to go to travis now.")
            webbrowser.open(
                "https://travis-ci.org/account/repositories", new=2, autoraise=True)
