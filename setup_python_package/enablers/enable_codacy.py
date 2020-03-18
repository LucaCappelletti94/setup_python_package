from ..utils import codacy_project_exists
import webbrowser


def enable_codacy(automatically_open_browser: bool):
    if not codacy_project_exists():
        print("You still need to create the codacy project.")
        if automatically_open_browser:
            input("Press any key to go to codacy now.")
            webbrowser.open(
                "https://app.codacy.com/wizard/projects", new=2, autoraise=True)
