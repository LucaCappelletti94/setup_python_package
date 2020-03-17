import json
import os


def load_configuration():
    with open("{}/config.json".format(os.path.dirname(os.path.abspath(__file__))), "r") as f:
        return json.load(f)
