from validate_version_code import validate_version_code
from setup_python_package.__version__ import __version__

def test_version():
    assert validate_version_code(__version__)