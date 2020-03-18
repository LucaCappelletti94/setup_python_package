from setup_python_package.utils.url_exists import url_exists

def test_url_exists():
    assert url_exists("https://www.google.com/")
    assert not url_exists("https://www.gooooogwfekwejfgkwegfjwhegfwghejgewkhwegkfwekwegfhogle.com/")