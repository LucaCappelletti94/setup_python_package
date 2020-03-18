from ..utils import sonar_project_exists
import webbrowser
from userinput import userinput
import subprocess
from ..enablers import enable_codeclimate


def validate_code_climate_code(code: str):
    return isinstance(code, str) and len(code) == 64


def get_code_climate_code():
    enable_codeclimate()
    print("Just go to repo settings/test_coverage and copy here the TEST REPORTER ID.")
    test_reported_id = userinput(
        "TEST REPORTER ID",
        validator=validate_code_climate_code,
        cache=False,
        maximum_attempts=50
    )
    subprocess.run([
        "travis",
        "encrypt",
        "CC_TEST_REPORTER_ID={}".format(test_reported_id),
        "--add"
    ], shell=True, input="\n", encoding='ascii')
