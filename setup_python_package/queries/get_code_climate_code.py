from userinput import userinput
import subprocess
from ..enablers import enable_codeclimate
import os


def validate_code_climate_code(code: str):
    return isinstance(code, str) and len(code) == 64


def get_code_climate_code(automatically_open_browser: bool):
    enable_codeclimate(automatically_open_browser)
    print("Just go to repo settings/test_coverage and copy here the TEST REPORTER ID.")
    test_reported_id = userinput(
        "TEST REPORTER ID",
        validator=validate_code_climate_code,
        cache=False
    )
    subprocess.run([
        "travis",
        "encrypt",
        "CC_TEST_REPORTER_ID={}".format(test_reported_id),
        "--add"
    ], shell=True, input="\n", stdout=open(os.devnull, 'w'), encoding='ascii')
