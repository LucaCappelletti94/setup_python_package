from ..utils import sonar_project_exists, load_repository_name, load_repository_author_name
import webbrowser
from userinput import userinput
import subprocess
from ..enablers import enable_codacy


def validate_codacy_code(code: str):
    return len(code) == 32


def get_codacy_code():
    enable_codacy()
    input("Press any key to go to the codacy project settings now to get the project token.")
    webbrowser.open(
        "https://app.codacy.com/app/{account}/{repository}/settings/integrations".format(
            account=load_repository_author_name(),
            repository=load_repository_name()
        ),
        new=2,
        autoraise=True
    )
    test_reported_id = userinput(
        "CODACY_PROJECT_TOKEN",
        validator=validate_codacy_code
    )
    subprocess.run(["travis", "encrypt", "CODACY_PROJECT_TOKEN={test_reported_id}".format(
        test_reported_id=test_reported_id), "--add"])
