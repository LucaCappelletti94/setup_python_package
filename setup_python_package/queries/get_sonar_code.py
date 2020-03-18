from userinput import userinput
import subprocess
from ..enablers import enable_sonar
from subprocess import PIPE


def validate_sonar_key(key: str) -> bool:
    return len(key) == 40


def get_sonar_code(automatically_open_browser: bool):
    enable_sonar(automatically_open_browser)
    print("Just copy the project key and paste it here.")
    sonar_key = userinput(
        "sonar project key",
        validator=validate_sonar_key,
        cache=False,
        maximum_attempts=50
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
