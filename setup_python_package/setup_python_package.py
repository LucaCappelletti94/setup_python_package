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


from .utils import coveralls_project_exists


def validate_sonar_key(key: str) -> bool:
    return len(key) == 40



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
    except (Exception, KeyboardInterrupt) as e:
        traceback.print_exc()
        print(e)
        print("Something went wrong!")
        if answer == "yes":
            repo.git.reset()
