from ..utils import sonar_project_exists
import webbrowser
from userinput import userinput
import subprocess
from ..enablers import enable_codeclimate


def validate_code_climate_code(code: str):
    return len(code) == 64


def get_code_climate_code():
    enable_codeclimate()
    print("Just go to repo settings/test_coverage and copy here the TEST REPORTER ID.")
    test_reported_id = userinput(
        "TEST REPORTER ID",
        validator=validate_code_climate_code
    )
    subprocess.run(["travis", "encrypt", "CC_TEST_REPORTER_ID={test_reported_id}".format(
        test_reported_id=test_reported_id), "--add"])
