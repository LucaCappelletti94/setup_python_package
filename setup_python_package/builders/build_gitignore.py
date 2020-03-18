import os


def build_gitignore():
    """Build gitignore file from model."""
    with open("{}/models/gitignore".format(os.path.dirname(os.path.abspath(__file__))), "r") as f:
        lines = f.readlines()
    path = ".gitignore"
    if os.path.exists(path):
        with open(path, "r") as d:
            lines = set(lines+d.readlines())
    with open(path, "w") as f:
        f.write("".join(sorted(lines)))
