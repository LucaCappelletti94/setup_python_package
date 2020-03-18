from setup_python_package import setup_python_package
from .utils import clone_test_repo, delete_test_repo


def auto_setup_python_package(label):
    if label.startswith("Please insert sonar project key:"):
        return "1111111111111111111111111111111111111111"
    if label.startswith("Please insert TEST REPORTER ID:"):
        return "c60e9f5957ec3318705c245a486a38258b4f52d63f090160dbbbd4043d265595"
    if label.startswith("Please insert Code climate maintainability badge"):
        return """.. image:: https://api.codeclimate.com/v1/badges/c79ec561e2fd2b91763c/maintainability
                    :target: https://codeclimate.com/github/LucaCappelletti94/compress_json/maintainability
                    :alt: Maintainability
                """
    if label.startswith("Please insert Code climate coverage badge:"):
        return """.. image:: https://api.codeclimate.com/v1/badges/c79ec561e2fd2b91763c/test_coverage
                    :target: https://codeclimate.com/github/LucaCappelletti94/compress_json/test_coverage
                    :alt: Test Coverage
                """
    if label.startswith("Please insert CODACY PROJECT TOKEN:"):
        return "d27d57c757a945bcb7ed975fd3d47a4e"
    if label.startswith("Please insert the Codacy Badge (RST format):"):
        return ".. image:: https://api.codacy.com/project/badge/Grade/b78d67845fe24f81919d95686ffb5bf8    :target: https://www.codacy.com/manual/LucaCappelletti94/keras_validation_sets?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=LucaCappelletti94/keras_validation_sets&amp;utm_campaign=Badge_Grade"
    open("../log.txt", "a").write(label+"\n")
    return "\n"


def test_setup_python_package(monkeypatch):
    open("../log.txt", "w").write("")
    clone_test_repo()
    monkeypatch.setattr('builtins.input', auto_setup_python_package)
    setup_python_package()
    delete_test_repo()
