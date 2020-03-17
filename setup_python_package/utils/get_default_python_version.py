import sys


def get_default_python_version():
    return "{major}.{minor}.0".format(
        major=sys.version_info.major,
        minor=sys.version_info.minor
    )
