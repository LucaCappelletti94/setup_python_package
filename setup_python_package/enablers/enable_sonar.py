from ..utils import sonar_project_exists
import webbrowser


def enable_sonar(automatically_open_browser: bool, project_key:str):
    if not sonar_project_exists(project_key):
        print("You still need to create the sonarcloud project.")
        if automatically_open_browser:
            input("Press any key to go to sonar now.")
            webbrowser.open("https://sonarcloud.io/projects/create",
                            new=2, autoraise=True)
