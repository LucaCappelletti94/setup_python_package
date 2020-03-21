import re
import os
import json
from ..utils import load_configuration


def extract_image_url(badge: str) -> str:
    return re.compile(r"image:: (.+)").findall(badge)[0]


def load_badges():
    with open(load_configuration()["badges"], "r") as f:
        return {
            name: badge for service in json.load(f).values() for name, badge in service.items()
        }


def validate_badge_generator(target:str):
    def validate_badge(badge: str):
        return isinstance(badge, str) and badge.startswith(".. image::") and ":target:" in badge and target in badge
    return validate_badge

def badge_exists(service: str) -> bool:
    if not os.path.exists(load_configuration()["badges"]):
        return False
    with open(load_configuration()["badges"], "r") as f:
        return service in json.load(f)


def add_badge(service: str, badge_name: str, badge: str):
    if os.path.exists(load_configuration()["badges"]):
        with open(load_configuration()["badges"], "r") as f:
            badges = json.load(f)
    else:
        badges = {}
    service_data = badges.get(service, {})
    service_data[badge_name] = badge.strip()
    badges[service] = service_data
    with open(load_configuration()["badges"], "w") as f:
        json.dump(badges, f)
