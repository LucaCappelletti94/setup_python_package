import re


def get_default_short_package_description() -> str:
    """Return short package description if one is detected."""
    try:
        with open("setup.py", "r") as f:
            return re.compile(
                r"""[(\s,]+description\s*=\s*["']([\s\S]*?)["']""").findall(f.read())[0].strip()
    except Exception:
        pass
    try:
        with open("README.md", "r") as f:
            return f.readlines()[1].strip()
    except Exception:
        pass
    try:
        with open("README.rst", "r") as f:
            return re.compile(
                r"\|\n\n([\s\S]+)\nHow do I install this package").findall(f.read())[0].strip()
    except Exception:
        pass
    return None
