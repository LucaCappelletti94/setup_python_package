import os
from pathlib import Path

def build_manifest():
    if not os.path.exists("MANIFEST.in"):
        Path("MANIFEST.in").touch()