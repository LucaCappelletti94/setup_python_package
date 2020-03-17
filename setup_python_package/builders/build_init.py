from pathlib import Path

def build_init(package: str):
    """Write package root init file."""
    Path("{package}/__init__.py".format(package=package)).touch()