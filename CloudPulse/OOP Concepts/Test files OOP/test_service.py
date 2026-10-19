
import sys
from pathlib import Path

# Find the parent OOP Concepts folder.
parent_folder = Path(__file__).resolve().parent.parent

# Tell Python to search that folder for modules.
sys.path.insert(0, str(parent_folder))

# Import the Service class.
from service import Service

def test_service_name():
    github = Service("GitHub", "https://github.com")
    assert github.name == "GitHub"


def test_service_url():
    github = Service("GitHub", "https://github.com")
    assert github.url == "https://github.com"


def test_service_has_check_health_method():
    github = Service("GitHub", "https://github.com")
    assert callable(github.check_health)


