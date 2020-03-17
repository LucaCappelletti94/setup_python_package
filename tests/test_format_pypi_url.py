from setup_python_package.utils.format_pypi_api_url import format_pypi_api_url

def test_format_pypi_api_url():
    assert format_pypi_api_url("numpy") == "https://pypi.org/pypi/numpy/json"