import re
import pypandoc


def get_default_long_package_description() -> str:
    """Return long package description if one is detected."""
    try:
        with open("README.md", "r") as f:
            return pypandoc.convert(
                source="\n".join(f.readlines()[1:]),
                to='rst',
                format='md'
            )
    except Exception:
        pass
    try:
        with open("README.rst", "r") as f:
            return re.compile(
                r"code_climate_coverage\|\n\n([\s\S]+)\n\.\. \|travis\|").findall(f.read())[0]
    except Exception:
        pass
    return None
