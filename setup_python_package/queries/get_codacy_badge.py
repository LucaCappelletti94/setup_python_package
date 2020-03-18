from ..utils import load_repository_name, load_repository_author_name
import webbrowser
from userinput import userinput
from ..badges import add_badge, validate_badge


def get_codacy_badge():
    print("Ok, now we are getting the RST project badge: remember RST!")
    print("It's the one starting with .. image::")
    input("Press any key to go to the codacy project settings now to get the project badge.")
    webbrowser.open(
        "https://app.codacy.com/app/{account}/{repository}/settings".format(
            account=load_repository_author_name(),
            repository=load_repository_name()
        ), new=2, autoraise=True)

    codacy_badge = userinput(
        "codacy badge",
        validator=validate_badge,
        cache=False
    )

    add_badge(
        "codacy",
        "codacy quality",
        "\n    ".join(codacy_badge.strip(".").split("    "))
    )
