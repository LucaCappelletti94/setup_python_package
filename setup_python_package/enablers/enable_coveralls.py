import webbrowser
from ..utils import coveralls_project_exists

def enable_coveralls():
    """Handle guided coveralls."""
    if not coveralls_project_exists():
        print("You still need to create the coveralls project.")
        input("Press any key to go to coveralls now.")
        webbrowser.open("https://coveralls.io/repos/new",
                        new=2, autoraise=True)