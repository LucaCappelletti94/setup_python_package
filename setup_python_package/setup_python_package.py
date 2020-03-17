from .environment import is_cwd_a_repository, is_travis_installed
from .utils import load_repository
from userinput import userinput
import traceback
import os


def start_build():
    os.makedirs(".spp_cache", exist_ok=True)
    # set_tests_directory()
    # build_gitignore()
    # build_version(package, version)
    # build_init(package)
    # build_tests(package)
    # build_setup(package, description, url, author, email)
    # build_sonar(package, account, url, version)
    # build_travis(package, account)
    # enable_coveralls(account, package)
    # build_readme(account, package, description)
    


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
