from glob import glob
import os
from validate_version_code import extract_version_code

def get_default_package_version():
    try:
        return extract_version_code()
    except ValueError:
        return "1.0.0"