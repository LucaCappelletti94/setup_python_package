import os
from ..queries import get_long_description


def build_readme(
    account: str,
    package: str,
    description: str
):
    with open("{}/models/readme".format(os.path.dirname(os.path.abspath(__file__))), "r") as source:
        with open("README.rst", "w") as sink:
            sink.write(source.read().format(
                package=package,
                account=account,
                description=description,
                long_description=get_long_description(),
                **get_badges()
            ))
