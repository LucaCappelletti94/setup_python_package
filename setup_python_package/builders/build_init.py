from pathlib import Path
import os


def build_init(package: str):
    """Write package root init file."""
    os.makedirs(package, exist_ok=True)
    Path("{package}/__init__.py".format(package=package)).touch()
