from ..utils import get_default_sonar_organization_key
from userinput import userinput


def get_sonar_organization_key() -> str:
    return userinput(
        name="sonar organization key",
        label="Enter a SonarCloud organization key.",
        default=get_default_sonar_organization_key(),
        validator="non_empty",
        cache=False
    )
