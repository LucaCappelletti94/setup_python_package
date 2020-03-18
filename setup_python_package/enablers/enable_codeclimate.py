from ..utils import codeclimate_project_exists
import webbrowser


def enable_codeclimate(automatically_open_browser: bool):
    if not codeclimate_project_exists():
        print("You still need to create the codeclimate project.")
        if automatically_open_browser:
            input("Press any key to go to codeclimate now.")
            webbrowser.open(
                "https://codeclimate.com/github/repos/new", new=2, autoraise=True)
