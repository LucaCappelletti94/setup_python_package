import shutil


def is_travis_installed() -> bool:
    """Return a boolean representing if travis gem is installed."""
    return shutil.which("travis") is not None
