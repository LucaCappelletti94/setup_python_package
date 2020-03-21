from ..utils import get_default_sonar_project_key
from userinput import userinput


def get_sonar_project_key() -> str:
    return userinput(
        name="sonar project key",
        label="Enter a SonarCloud project key.",
        default=get_default_sonar_project_key(),
        validator="non_empty",
        cache=False
    )
