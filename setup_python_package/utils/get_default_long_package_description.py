import re
import pypandoc


def get_default_long_package_description() -> str:
    """Return long package description if one is detected."""
    try:
        with open("README.md", "r") as f:
            return pypandoc.convert_text(
                source="\n".join(f.readlines()[1:]),
                to='rst',
                format='md'
            ).strip()
    except Exception:
        pass
    try:
        with open("README.rst", "r") as f:
            return re.compile(
                r"code_climate_coverage\|\n\n([\s\S]+)\n\.\. \|travis\|").findall(f.read())[0].strip()
    except Exception:
        pass
    return "TODO: add long description of package here."
