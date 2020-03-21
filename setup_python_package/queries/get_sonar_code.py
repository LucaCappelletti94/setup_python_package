from userinput import userinput
import subprocess
from ..enablers import enable_sonar
from subprocess import PIPE


def validate_sonar_key(key: str) -> bool:
    return isinstance(key, str) and len(key) == 40


def get_sonar_code(automatically_open_browser: bool, project_key:str):
    enable_sonar(automatically_open_browser, project_key)
    print("Now I need a SonarCloud code for your project.")
    print(
        "You can find such a code when creating a new sonar project,\n"
        "or by going to https://sonarcloud.io/account/security/ and create\n"
        "a new token. These tokens are strings of 40 characters."
    )
    sonar_key = userinput(
        "SonarCloud access token",
        validator=validate_sonar_key,
        cache=False
    )
    result = subprocess.Popen(
        [
            'travis',
            'encrypt',
            sonar_key
        ],
        stdout=PIPE,
        shell=True
    )
    result.wait()
    out, _ = result.communicate()
    result.stdout.close()
    return out.decode("utf-8").strip().strip('"')
