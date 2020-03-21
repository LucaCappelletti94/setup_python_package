from .environment import is_cwd_a_repository, is_travis_installed
from .utils import load_repository
from .queries import get_package_name, get_short_description, get_package_version, get_sonar_organization_key, get_sonar_project_key
from .builders import build_readme, build_gitignore, build_version, build_init, build_tests, build_setup, build_travis, build_sonar
from userinput import userinput
from .enablers import enable_coveralls
import traceback
import os



def start_build():
    os.makedirs(".spp_cache", exist_ok=True)
    package = get_package_name()
    version = get_package_version()
    automatically_open_browser = userinput(
        "open_browser",
        label="Do you want me to open the browser automatically?",
        default="yes",
        validator="human_bool",
        sanitizer="human_bool",
        cache=False
    )
    short_description = get_short_description()
    build_gitignore()
    build_version(package, version)
    build_init(package)
    build_tests(package)
    build_setup(package, short_description)

    organization_key = get_sonar_organization_key()
    project_key = get_sonar_project_key()

    build_sonar(
        package=package,
        version=version,
        organization_key=organization_key,
        project_key=project_key
    )
    build_travis(package, automatically_open_browser, project_key, organization_key)
    enable_coveralls(automatically_open_browser)
    build_readme(package, short_description, project_key)



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
        repo.git.clean('-xdf')
        repo.git.reset()
        if not isinstance(e, KeyboardInterrupt):
            raise e
        else:
            print("User interrupted procedure.")