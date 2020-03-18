import re
import os
import json


def extract_image_url(badge: str) -> str:
    return re.compile(r"image:: (.+)").findall(badge)[0]


def load_badges():
    with open(".spp_cache/badges.json", "r") as f:
        return {
            name: badge for service in json.load(f).values() for name, badge in service.items()
        }


def validate_badge(badge: str):
    return isinstance(badge, str) and badge.startswith(".. image::") and ":target:" in badge


def badge_exists(service: str) -> bool:
    if not os.path.exists(".spp_cache/badges.json"):
        return False
    with open(".spp_cache/badges.json", "r") as f:
        return service in json.load(f)


def add_badge(service: str, badge_name: str, badge: str):
    if os.path.exists(".spp_cache/badges.json"):
        with open(".spp_cache/badges.json", "r") as f:
            badges = json.load(f)
    else:
        badges = {}
    service_data = badges.get(service, {})
    service_data[badge_name] = badge.strip()
    badges[service] = service_data
    with open(".spp_cache/badges.json", "w") as f:
        json.dump(badges, f)
