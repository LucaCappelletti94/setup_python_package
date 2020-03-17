from ..utils import sonar_project_exists
import webbrowser
from userinput import userinput
import subprocess


def validate_sonar_key(key: str) -> bool:
    return len(key) == 40

def get_sonar_code(account: str, package: str):
    if not sonar_project_exists(account, package):
        print("You still need to create the sonarcloud project.")
        input("Press any key to go to sonar now.")
        webbrowser.open("https://sonarcloud.io/projects/create",
                        new=2, autoraise=True)
    print("Just copy the project key and paste it here.")
    sonar_key = userinput(
        "sonar project key",
        validator=validate_sonar_key
    )
    result = subprocess.run(
        [
            'travis',
            'encrypt',
            sonar_key
        ],
        capture_output=True
    )
    return result.stdout.decode("utf-8").strip().strip('"')