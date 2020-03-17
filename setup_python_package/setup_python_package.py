from .environment import is_cwd_a_repository, is_travis_installed
from .utils import load_repository
from .queries import get_package_name, get_short_description
from .builders import build_readme, build_gitignore, build_version, build_init
from userinput import userinput
import traceback
import os


def start_build():
    os.makedirs(".spp_cache", exist_ok=True)
    package = get_package_name()
    os.makedirs(package, exist_ok=True)
    short_description = get_short_description()
    build_gitignore()
    build_version(package)
    build_init(package)
    # build_tests(package)
    # build_setup(package, description, url, author, email)
    # build_sonar(package, account, url, version)
    # build_travis(package, account)
    # enable_coveralls(account, package)
    build_readme(package, short_description)



def setup_python_package():
    if not is_cwd_a_repository():
        print("Please run setup_python_package from within a valid git repository.")
        return
    if not is_travis_installed():
        print("We could not detect the travis gem. Please install travis by running (sudo) gem install travis.")
        return

    try:
        repo = load_repository()
        repo.git.add("--all")
        repo.index.commit("[SPP] Created a backup.")
        start_build()
        repo.git.add("--all")
        repo.index.commit("[SPP] Completed setup and CI integration.")
    except (Exception, KeyboardInterrupt) as e:
        traceback.print_exc()
        print(e)
        print("Something went wrong!")
        repo.git.reset()
