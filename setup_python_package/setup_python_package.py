import os
import re
import json
import git
import requests
from validate_email import validate_email
from validate_version_code import validate_version_code, extract_version_code
from typing import Callable
from pathlib import Path
from validators import url as validate_url
import webbrowser
import sys
import shutil
import subprocess
import traceback

cwd = os.path.dirname(os.path.realpath(__file__))
with open("{cwd}/models/config.json".format(cwd=cwd), "r") as f:
    config = json.load(f)


def user_input(name: str, candidate=None, validator: Callable = None, incipit: str = "Please insert ", lines=1) -> str:
    candidate_sub = candidate
    if isinstance(candidate, str) and (len(candidate) > 100 or "\n" in candidate):
        candidate_sub = candidate_sub.replace("\n", " ")
        if len(candidate_sub) > 100:
            candidate_sub = "{first} [...] {last}".format(
                first=candidate_sub[:50],
                last=candidate_sub[-50:]
            ).strip()
    candidate_wrapper = "" if candidate is None else " [{candidate}]".format(
        candidate=candidate_sub)
    while True:
        choice = []
        message = "{incipit}{name}{candidate_wrapper}: ".format(
            incipit=incipit,
            name=name,
            candidate_wrapper=candidate_wrapper
        )
        for i in range(lines):
            choice.append(input(message if i == 0 else "").strip())

        choice = "\n".join(choice)
        if not choice:
            choice = candidate
        if validator is None or choice is not None and validator(choice):
            return choice
        print("Invalid value '{choice}' for {name}.".format(
            choice=choice,
            name=name
        ))


def url_exists(url: str, max_redirect: int = 10):
    session = requests.Session()
    session.max_redirects = max_redirect
    try:
        return session.get(url).status_code == 200
    except requests.TooManyRedirects:
        return False


def package_exists(package: str) -> bool:
    return url_exists("https://pypi.org/project/{package}/".format(package=package))


def is_owner(package: str, url: str):
    return url in requests.get(
        "https://pypi.org/project/{package}/".format(package=package)
    ).text


def validate_boolean_answer(answer: str) -> bool:
    return answer.lower() in ("yes", "no")


def is_valid_package_name(url: str) -> Callable:
    def wrapper(package: str):
        if package_exists(package) and not is_owner(package, url):
            print("Package {package} already exists on pipy!".format(
                package=package))
            print(
                "Since I don't see the package url in the repo, I believe you are not the owner.")
            return False
        return all([
            c not in package for c in ("-", ".", " ")
        ])
    return wrapper


def detect_package_name(url: str) -> str:
    return user_input(
        "package name",
        os.getcwd().split("/")[-1],
        is_valid_package_name(url)
    )


def detect_package_description() -> str:
    description = None
    try:
        if os.path.exists("setup.py"):
            with open("setup.py", "r") as f:
                description = re.compile(
                    r"""[(\s,]+description\s*=\s*["']([\s\S]*?)["']""").findall(f.read())[0]
        elif os.path.exists("README.md"):
            with open("README.md", "r") as f:
                description = f.readlines()[1].strip()
        elif os.path.exists("README.rst"):
            with open("README.rst", "r") as f:
                description = re.compile(
                    r"\|\n\n([\s\S]+)\nHow do I install this package").findall(f.read())[0]
    except Exception:
        pass

    return user_input(
        "package description",
        description,
        validator=lambda x: isinstance(x, str) and len(x.strip()) > 0
    ).strip()


def detect_package_long_description() -> str:
    description = None
    try:
        if os.path.exists("README.md"):
            with open("README.md", "r") as f:
                description = "\n".join(f.readlines()[1:])
        elif os.path.exists("README.rst"):
            with open("README.rst", "r") as f:
                description = re.compile(
                    r"code_climate_coverage\|\n\n([\s\S]+)\n\.\. \|travis\|").findall(f.read())[0]
    except Exception:
        pass

    return user_input(
        "package long description",
        description,
        validator=lambda x: isinstance(x, str) and len(x.strip()) > 0
    )


def detect_package_author(author: str):
    return user_input(
        "author name",
        author
    )


def detect_python_version():
    return user_input(
        "python version",
        "{major}.{minor}".format(
            major=sys.version_info.major,
            minor=sys.version_info.minor
        ))


def detect_package_email(email: str):
    return user_input(
        "author email",
        email,
        validate_email
    )


def detect_package_version(package: str):
    default = extract_version_code(package) if os.path.exists(
        "{package}/__version__.py".format(package=package)) else "1.0.0"
    return user_input(
        "package version",
        default,
        validate_version_code
    )


def detect_package_url(url: str):
    return user_input(
        "package url",
        url,
        validate_url
    )


def load_repo():
    return git.Repo(os.getcwd())


def is_repo() -> bool:
    try:
        load_repo()
        return True
    except git.InvalidGitRepositoryError:
        return False


def set_tests_directory():
    config["tests_directory"] = user_input(
        "tests directory",
        config["tests_directory"]
    )


def build_gitignore():
    with open("{cwd}/models/gitignore".format(cwd=cwd), "r") as source:
        path = ".gitignore"
        rows = source.readlines()
        if os.path.exists(path):
            with open(path, "r") as gitignore:
                rows = set([e.strip()
                            for e in gitignore.readlines() + rows if e.strip()])
        with open(path, "w") as gitignore:
            gitignore.write("\n".join(rows))


def build_version(package: str, version: str):
    with open("{cwd}/models/version".format(cwd=cwd), "r") as source:
        with open("{package}/__version__.py".format(package=package), "w") as sink:
            sink.write(source.read().format(version=version, package=package))


def build_init(package: str):
    Path("{package}/__init__.py".format(package=package)).touch()


def build_version_test(package: str):
    with open("{cwd}/models/version_test".format(cwd=cwd), "r") as source:
        with open("{tests_directory}/test_version.py".format(tests_directory=config["tests_directory"]), "w") as sink:
            sink.write(source.read().format(package=package))


def build_tests(package: str):
    os.makedirs(config["tests_directory"], exist_ok=True)
    build_init(config["tests_directory"])
    build_version_test(package)


def build_setup(package: str, short_description: str, url: str, author: str, email: str):
    if not os.path.exists("MANIFEST.in"):
        Path("MANIFEST.in").touch()
    path = "setup.py"
    test_dependencies = config["test_dependencies"]
    install_dependencies = []
    if os.path.exists(path):
        with open(path, "r") as f:
            content = f.read()
        try:
            if "test_deps" in content:
                test_dependencies = list(set(test_dependencies + [
                    key.strip("\"' \n") for key in re.compile(r"test_deps\s*=\s*\[([\s\S]+?)\]").findall(content)[0].split(",")
                ]))
        except Exception:
            pass
        try:
            if "install_requires" in content:
                install_dependencies = list(set(install_dependencies+[
                    key.strip("\"' \n") for key in re.compile(r"install_requires\s*=\s*\[([\s\S]+?)\]").findall(content)[0].split(",")
                ]))
        except Exception:
            pass

        path = "suggested_setup.py"
        print("I am not touching your setup.py, you'll need to update it yourself.")
        print(
            "I have generated a suggested one called {path}".format(path=path))

    with open("{cwd}/models/setup".format(cwd=cwd), "r") as source:
        with open(path, "w") as sink:
            sink.write(source.read().format(
                package=package,
                short_description=short_description,
                url=url,
                author=author,
                email=email,
                install_dependencies=json.dumps(
                    install_dependencies, indent=4),
                test_dependencies=json.dumps(test_dependencies, indent=4)
            ))


def build_readme(account: str, package: str, description: str):
    with open("{cwd}/models/readme".format(cwd=cwd), "r") as source:
        long_description = detect_package_long_description()
        with open("README.rst", "w") as sink:
            sink.write(source.read().format(
                package=package,
                account=account,
                description=description,
                long_description=long_description,
                **get_badges()
            ))


def build_sonar(package: str, account: str, url: str, version: str):
    with open("{cwd}/models/sonar".format(cwd=cwd), "r") as source:
        with open("sonar-project.properties", "w") as sink:
            sink.write(source.read().format(
                package=package,
                account=account,
                account_lower=account.lower(),
                url=url,
                version=version,
                tests_directory=config["tests_directory"]
            ))


def validate_sonar_key(key: str) -> bool:
    return len(key) == 40


def get_sonar_code(package: str, account: str):
    url = "https://sonarcloud.io/api/project_badges/measure?project={account}_{package}&metric=coverage".format(
        account=account,
        package=package
    )
    if "Project has not been found" in requests.get(url).text:
        print("You still need to create the sonarcloud project.")
        print("Just copy the project key and paste it here.")
        input("Press any key to go to sonar now.")
        webbrowser.open("https://sonarcloud.io/projects/create",
                        new=2, autoraise=True)
    return user_input(
        "sonar project key",
        validator=validate_sonar_key
    )


def validate_travis_key(key: str) -> bool:
    return key.endswith("=") and len(key) == 684


def get_travis_code(package: str, account: str):
    if not url_exists("https://travis-ci.org/{account}/{package}.png".format(account=account, package=package), max_redirect=2):
        print("You still need to create the travis project.")
        input("Press any key to go to travis now.")
        webbrowser.open(
            "https://travis-ci.org/account/repositories", new=2, autoraise=True)
    sonar_code = get_sonar_code(package, account)
    print("Please run the following into a terminal window in this repository:")
    print("travis encrypt {sonar_code}".format(sonar_code=sonar_code))
    print("Copy only the generate key here, it looks like this:")
    print("secure: \"very_long_key\" ")
    return user_input(
        "travis project key",
        validator=validate_travis_key
    )


def validate_code_climate_code(code: str):
    return len(code) == 64


def extract_image_url(badge: str) -> str:
    return re.compile(r"image:: (.+)").findall(badge)[0]


def add_code_climate(account: str, package: str):
    service = "code_climate"
    if badge_exists(service):
        return
    print("="*20)
    print("Setting up Code Climate!")
    if not url_exists("https://codeclimate.com/github/{account}/{package}".format(account=account, package=package)):
        print("You might need to create the code climate project.")
        input("Press any key to go to code climate now.")
        webbrowser.open(
            "https://codeclimate.com/github/repos/new", new=2, autoraise=True)
    input("Press any key to go to code climate package.")
    webbrowser.open(
        "https://codeclimate.com/github/{account}/{package}".format(account=account, package=package), new=2, autoraise=True)
    print("Just go to repo settings/test_coverage and copy here the TEST REPORTER ID.")
    test_reported_id = user_input(
        "TEST REPORTER ID",
        validator=validate_code_climate_code
    )
    subprocess.run(["travis", "encrypt", "CC_TEST_REPORTER_ID={test_reported_id}".format(
        test_reported_id=test_reported_id), "--add"])

    print("Ok, now we are getting the RST project badges: remember RST!")
    print("They are the ones starting with .. image::")
    input("Press any key to go to the code climate project settings now to get the project badge.")
    webbrowser.open(
        "https://codeclimate.com/github/{account}/{package}/badges".format(account=account, package=package), new=2, autoraise=True)
    add_badge(service, "{service}_maintainability_url".format(service=service), extract_image_url(user_input(
        "Code climate maintainability badge",
        validator=validate_badge,
        lines=3
    ).strip(".")))
    add_badge(service, "{service}_coverage_url".format(service=service), extract_image_url(user_input(
        "Code climate coverage badge",
        validator=validate_badge,
        lines=3
    ).strip(".")))


def validate_codacy_code(code: str):
    return len(code) == 32


def validate_badge(badge: str):
    return badge.startswith(".. image::") and ":target:" in badge


def badge_exists(service: str) -> bool:
    if not os.path.exists(".spp_cache/badges.json"):
        return False
    with open(".spp_cache/badges.json", "r") as f:
        return service in json.load(f)


def get_badges():
    with open(".spp_cache/badges.json", "r") as f:
        return {
            name: badge for service in json.load(f).values() for name, badge in service.items()
        }


def add_badge(service: str, badge_name: str, badge: str):
    if os.path.exists(".spp_cache/badges.json"):
        with open(".spp_cache/badges.json", "r") as f:
            badges = json.load(f)
    else:
        badges = {}
    service_data = badges.get(service, {})
    service_data[badge_name] = badge.strip()
    badges[service] = service_data
    with open(".spp_cache/badges.json", "w") as f:
        json.dump(badges, f)


def add_codacy(account: str, package: str):
    service = "codacy"
    if badge_exists(service):
        return
    print("="*20)
    print("Setting up Codacy!")
    if not url_exists("https://app.codacy.com/project/{account}/{package}/dashboard".format(account=account, package=package)):
        print("You still need to create the codacy project.")
        input("Press any key to go to codacy now.")
        webbrowser.open("https://app.codacy.com/wizard/projects",
                        new=2, autoraise=True)
    input("Press any key to go to the codacy project settings now to get the project token.")
    webbrowser.open("https://app.codacy.com/app/{account}/{package}/settings/integrations".format(
        account=account, package=package), new=2, autoraise=True)
    test_reported_id = user_input(
        "CODACY_PROJECT_TOKEN",
        validator=validate_codacy_code
    )
    subprocess.run(["travis", "encrypt", "CODACY_PROJECT_TOKEN={test_reported_id}".format(
        test_reported_id=test_reported_id), "--add"])
    print("Ok, now we are getting the RST project badge: remember RST!")
    print("It's the one starting with .. image::")
    input("Press any key to go to the codacy project settings now to get the project badge.")
    webbrowser.open("https://app.codacy.com/app/{account}/{package}/settings".format(
        account=account, package=package), new=2, autoraise=True)
    add_badge(service, service, "\n    ".join(user_input(
        "codacy badge",
        validator=validate_badge
    ).strip(".").split("    ")))


def build_travis(package: str, account: str):
    if not os.path.exists(".travis.yml"):
        with open("{cwd}/models/travis".format(cwd=cwd), "r") as source:
            with open(".travis.yml", "w") as sink:
                sink.write(source.read().format(
                    package=package,
                    account=account,
                    account_lower=account.lower(),
                    sonar_travis_code=get_travis_code(package, account),
                    python_version=detect_python_version()
                ))
    if user_input(
            "Do you want to add code climate?",
            "yes",
            validator=validate_boolean_answer,
            incipit=""
        ).lower() == "yes":
        add_code_climate(account, package)
    if user_input(
            "Do you want to add codacy?",
            "yes",
            validator=validate_boolean_answer,
            incipit=""
        ).lower() == "yes":
        add_codacy(account, package)


def enable_coveralls(account: str, package: str):
    if not url_exists("https://coveralls.io/github/{account}/{package}".format(account=account, package=package)):
        print("You still need to create the coveralls project.")
        input("Press any key to go to coveralls now.")
        webbrowser.open("https://coveralls.io/repos/new",
                        new=2, autoraise=True)


def build(repo):
    os.makedirs(".spp_cache", exist_ok=True)
    url = detect_package_url(repo.remote().url.split(".git")[0])
    package = detect_package_name(url)
    master = repo.head.reference
    author = detect_package_author(master.commit.author.name)
    email = detect_package_email(master.commit.author.email)
    account = url.split("/")[-2]
    os.makedirs(package, exist_ok=True)
    description = detect_package_description()
    version = detect_package_version(package)
    set_tests_directory()
    build_gitignore()
    build_version(package, version)
    build_init(package)
    build_tests(package)
    build_setup(package, description, url, author, email)
    build_sonar(package, account, url, version)
    build_travis(package, account)
    enable_coveralls(account, package)
    build_readme(account, package, description)
    if os.path.exists("README.md"):
        os.remove("README.md")
    repo.git.add("--all")
    repo.index.commit(
        "[SPP] Completed basic setup package and CI integration.")


def setup_python_package():
    if not is_repo():
        print("Please run setup_python_package from within a valid git repository.")
        return
    repo = load_repo()
    try:
        answer = user_input(
            "Do you want to create a backup commit?",
            "yes",
            validator=validate_boolean_answer,
            incipit=""
        ).lower()
        if answer == "yes":
            repo.git.add("--all")
            repo.index.commit("[SPP] Created a backup.")
        build(repo)
    except Exception as e:
        traceback.print_exc()
        print(e)
        print("Something went wrong!")
        if answer == "yes":
            repo.git.reset()
