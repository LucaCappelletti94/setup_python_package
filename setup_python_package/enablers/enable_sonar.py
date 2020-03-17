from ..utils import sonar_project_exists
import webbrowser


def enable_sonar():
    if not sonar_project_exists():
        print("You still need to create the sonarcloud project.")
        input("Press any key to go to sonar now.")
        webbrowser.open("https://sonarcloud.io/projects/create",
                        new=2, autoraise=True)