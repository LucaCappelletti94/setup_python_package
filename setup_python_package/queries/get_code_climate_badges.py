from ..utils import load_repository_author_name, load_repository_name
from ..badges import add_badge, validate_badge, extract_image_url
from userinput import userinput
import webbrowser


def get_code_climate_badges():
    print("Ok, now we are getting the RST project badges: remember RST!")
    print("They are the ones starting with .. image::")
    input("Press any key to go to the code climate project settings now to get the project badge.")
    webbrowser.open(
        "https://codeclimate.com/github/{account}/{package}/badges".format(
            account=load_repository_author_name(),
            package=load_repository_name()
        ), new=2, autoraise=True)
    add_badge("code_climate", "code_climate_maintainability_url", extract_image_url(userinput(
        "Code climate maintainability badge",
        validator=validate_badge
    ).strip(".")))
    add_badge("code_climate", "code_climate_coverage_url", extract_image_url(userinput(
        "Code climate coverage badge",
        validator=validate_badge
    ).strip(".")))
