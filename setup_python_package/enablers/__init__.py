from .enable_coveralls import enable_coveralls
from .enable_travis import enable_travis
from .enable_sonar import enable_sonar
from .enable_codacy import enable_codacy
from .enable_codeclimate import enable_codeclimate

__all__ = [
    "enable_coveralls",
    "enable_travis",
    "enable_sonar",
    "enable_codacy",
    "enable_codeclimate"
]