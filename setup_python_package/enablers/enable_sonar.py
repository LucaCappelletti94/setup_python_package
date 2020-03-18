from ..utils import sonar_project_exists
import webbrowser
from environments_utils import is_stdout_enabled

def enable_sonar():
    if not sonar_project_exists():
        print("You still need to create the sonarcloud project.")
        if is_stdout_enabled():
            input("Press any key to go to sonar now.")
            webbrowser.open("https://sonarcloud.io/projects/create",
                            new=2, autoraise=True)