from setup_python_package.utils.load_repository import load_repository_url


def test_load_repository_url():
    assert load_repository_url() == "https://github.com/LucaCappelletti94/setup_python_package"
