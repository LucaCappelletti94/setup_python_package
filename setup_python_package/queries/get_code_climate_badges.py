from ..utils import load_repository_organization, load_repository_name
from ..badges import add_badge, extract_image_url
from bs4 import BeautifulSoup
import requests


def get_code_climate_badges():
    url = "https://codeclimate.com/github/{organization}/{repository}/badges".format(
        organization=load_repository_organization(),
        repository=load_repository_name()
    )

    soup = BeautifulSoup(requests.get(url).text, 'html.parser')

    add_badge("code_climate", "code_climate_maintainability_url", extract_image_url(
        soup.find(id="maintainability-restructured").text
    ))
    add_badge("code_climate", "code_climate_coverage_url", extract_image_url(
        soup.find(id="test-coverage-restructured").text
    ))
