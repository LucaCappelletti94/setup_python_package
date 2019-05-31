import os
import json
import git
import requests
from validate_email import validate_email
from validate_version_code import validate_version_code
from typing import Callable
from pathlib import Path
from validators import url as validate_url
import webbrowser  
import sys

cwd = os.path.dirname(os.path.realpath(__file__))
with open("{cwd}/models/config.json".format(cwd=cwd), "r") as f:
    config = json.load(f)

def user_input(name:str, candidate=None, validator:Callable=None)->str:
    candidate_wrapper = "" if candidate is None else " [{candidate}]".format(candidate=candidate)
    while True:
        choice = input("Please insert {name}{candidate_wrapper}: ".format(
            name=name,
            candidate_wrapper=candidate_wrapper
        )).strip()
        if not choice:
            choice = candidate
        if validator is None or choice is not None and validator(choice):
            return choice
        print("Invalid value '{choice}' for {name}.".format(
            choice=choice,
            name=name
        ))

def url_exists(url:str):
    return requests.get(url).status_code == 200

def package_exists(package:str)->bool:
    return url_exists("https://pypi.org/project/{package}/".format(package=package))

def is_valid_package_name(name:str)->bool:
    if package_exists(name):
        print("Package {name} already exists on pipy!".format(name=name))
        return False
    return all([
        c not in name for c in ("-", ".", " ")
    ])

def detect_package_name()->str:
    return user_input(
        "package name",
        os.getcwd().split("/")[-1],
        is_valid_package_name
    )

def is_valid_description(description:str)->bool:
    return len(description)>5

def detect_package_description()->str:
    description = None
    if os.path.exists("README.md"):
        with open("README.md", "r") as f:
            description = f.readlines()[1].strip()

    return user_input(
        "package description",
        description,
        is_valid_description
    )

def detect_package_author(author:str):
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

def detect_package_email(email:str):
    return user_input(
        "author email",
        email,
        validate_email
    )

def detect_package_version():
    return user_input(
        "package version",
        "1.0.0",
        validate_version_code
    )

def detect_package_url(url:str):
    return user_input(
        "package url",
        url,
        validate_url
    )

def load_repo():
    return git.Repo(os.getcwd())

def is_repo()->bool:
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
        with open(".gitignore", "w") as sink:
            sink.write(source.read())

def build_version(package:str, version:str):
    with open("{cwd}/models/version".format(cwd=cwd), "r") as source:
        with open("{package}/__version__.py".format(package=package), "w") as sink:
            sink.write(source.read().format(version=version, package=package))

def build_init(package:str):
    Path("{package}/__init__.py".format(package=package)).touch()

def build_version_test(package:str):
    with open("{cwd}/models/version_test".format(cwd=cwd), "r") as source:
        with open("{tests_directory}/test_version.py".format(tests_directory=config["tests_directory"]), "w") as sink:
            sink.write(source.read().format(package=package))

def build_tests(package:str):
    os.makedirs(config["tests_directory"], exist_ok=True)
    build_init(config["tests_directory"])    
    build_version_test(package)


def build_setup(package:str, short_description:str, url:str, author:str, email:str):
    Path("MANIFEST.in").touch()
    with open("{cwd}/models/setup".format(cwd=cwd), "r") as source:
        with open("setup.py", "w") as sink:
            sink.write(source.read().format(
                package=package,
                short_description=short_description,
                url=url,
                author=author,
                email=email
            ))

def build_readme(account:str, package:str, description:str):
    with open("{cwd}/models/readme".format(cwd=cwd), "r") as source:
        with open("README.rst", "w") as sink:
            sink.write(source.read().format(
                package=package,
                account=account,
                description=description
            ))

def build_sonar(package:str, account:str, url:str, version:str):
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

def validate_sonar_key(key:str)->bool:
    return len(key)==40

def get_sonar_code(package:str, account:str):
    print("You might need to create the sonarcloud project.")
    print("Just copy the project key and paste it here.")
    input("Press any key to go to sonar now.")
    webbrowser.open("https://sonarcloud.io/projects/create", new=2, autoraise=True)
    return user_input(
        "sonar project key",
        validator=validate_sonar_key
    )

def validate_travis_key(key:str)->bool:
    return key.endswith("=") and len(key)==684

def get_travis_code(package:str, account:str):
    print("You might need to create the travis project.")
    input("Press any key to go to travis now.")
    webbrowser.open("https://travis-ci.org/account/repositories", new=2, autoraise=True)
    sonar_code = get_sonar_code(package, account)
    print("Please run the following into a terminal window in this repository:")
    print("travis encrypt {sonar_code}".format(sonar_code=sonar_code))
    print("Copy only the generate key here, it looks like this:")
    print("secure: \"very_long_key\" ")
    return user_input(
        "travis project key",
        validator=validate_travis_key
    )

def build_travis(package:str, account:str):
    with open("{cwd}/models/travis".format(cwd=cwd), "r") as source:
        with open(".travis.yml", "w") as sink:
            sink.write(source.read().format(
                package=package,
                account=account,
                account_lower=account.lower(),
                travis_code=get_travis_code(package, account),
                python_version=detect_python_version()
            ))

def validate_coveralls_key(key:str)->bool:
    return len(key)==33

def get_coveralls_code(account:str, package:str):
    if not url_exists("https://coveralls.io/github/{account}/{package}".format(account=account, package=package)):
        print("You still need to create the coveralls project.")
        print("Just copy the repo_token and paste it here.")
        input("Press any key to go to coveralls now.")
        webbrowser.open("https://coveralls.io/repos/new", new=2, autoraise=True)
    return user_input(
        "coveralls repo_token",
        validator=validate_coveralls_key
    )

def build_coveralls(account:str, package:str):
    with open("{cwd}/models/coveralls".format(cwd=cwd), "r") as source:
        with open(".coveralls.yml", "w") as sink:
            sink.write(source.read().format(
                repo_token=get_coveralls_code(account, package)
            ))

def setup_python_package():
    if not is_repo():
        print("Please run setup_python_package from within a valid git repository.")
        return
    package = detect_package_name()
    repo = load_repo()
    master = repo.head.reference
    author = detect_package_author(master.commit.author.name)
    email = detect_package_email(master.commit.author.email)
    url = detect_package_url(repo.remote().url.split(".git")[0])
    account = url.split("/")[-2]
    os.makedirs(package, exist_ok=True)
    description = detect_package_description()
    version = detect_package_version()
    set_tests_directory()
    build_gitignore()
    build_version(package, version)
    build_init(package)
    build_tests(package)
    build_setup(package, description, url, author, email)
    build_readme(account, package, description)
    build_sonar(package, account, url, version)
    build_travis(package, account)
    build_coveralls(account, package)
    if os.path.exists("README.md"):
        os.remove("README.md")
    repo.git.add("--all")
    repo.index.commit("[SETUP PYTHON PACKAGE] Completed basic setup package and CI integration.")