from ..utils import codeclimate_project_exists
import webbrowser
from environments_utils import is_stdout_enabled


def enable_codeclimate():
    if not codeclimate_project_exists():
        print("You still need to create the codeclimate project.")
        if is_stdout_enabled():
            input("Press any key to go to codeclimate now.")
            webbrowser.open(
                "https://codeclimate.com/github/repos/new", new=2, autoraise=True)
