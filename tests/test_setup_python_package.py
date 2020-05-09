from setup_python_package import setup_python_package
from .utils import clone_test_repo, delete_test_repo
import os
from httmock import urlmatch, HTTMock


def auto_setup_python_package(label):
    if label.startswith("Do you want me to open the browser automatically?"):
        return "no"
    if label.startswith("Please insert SonarCloud access token"):
        return "1111111111111111111111111111111111111111"
    if label.startswith("Please insert TEST REPORTER ID:"):
        return "c60e9f5957ec3318705c245a486a38258b4f52d63f090160dbbbd4043d265595"
    if label.startswith("Please insert CODACY PROJECT TOKEN:"):
        return "d27d57c757a945bcb7ed975fd3d47a4e"
    if label.startswith("Please insert the Codacy Badge (RST format):"):
        return ".. image:: https://api.codacy.com/project/badge/Grade/b78d67845fe24f81919d95686ffb5bf8    :target: https://www.codacy.com/manual/LucaCappelletti94/keras_validation_sets?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=LucaCappelletti94/keras_validation_sets&amp;utm_campaign=Badge_Grade"
    return "\n"


@urlmatch(path="/github/LucaCappelletti94/setup_python_package_test_reporitory/badges")
def mock_code_climate(url, request):
    with open("{}/mocked_code_climate.html".format(os.path.dirname(os.path.abspath(__file__))), "r") as f:
        return {
            'status_code': 200,
            'content': f.read()
        }


def test_setup_python_package(monkeypatch):
    clone_test_repo()
    monkeypatch.setattr('builtins.input', auto_setup_python_package)
    with HTTMock(mock_code_climate):
        setup_python_package()
        os.remove("setup.py")
        setup_python_package()
        setup_python_package()
        try:
            targets = [
                "MANIFEST.in",
                "README.rst",
                ".gitignore",
                "setup_python_package_test_reporitory/__version__.py",
                "setup_python_package_test_reporitory/__init__.py"
            ]
            for target in targets:
                with open(target, "r") as f1:
                    d1 = f1.read()
                with open(f"../expected/{target}", "r") as f2:
                    d2 = f2.read()
                assert d1 == d2
            delete_test_repo()
        except (Exception, AssertionError) as e:
            delete_test_repo()
            raise e
