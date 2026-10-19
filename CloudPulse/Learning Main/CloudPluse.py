
# Project: CloudPulse
# Import the existing performance classifier.
from performance import classify_performance

# Import the Service class from the OOP Concepts folder.
import sys
from pathlib import Path

project_folder = Path(__file__).resolve().parent.parent
oop_folder = project_folder / "OOP Concepts"
sys.path.insert(0, str(oop_folder))

from service import Service


# Websites that CloudPulse will monitor.
services = [
    Service("Example Website", "https://example.com"),
    Service("Python Website", "https://www.python.org"),
    Service("GitHub", "https://github.com"),
    Service("Google", "https://www.google.com"),
    Service("ARU", "https://www.aru.ac.uk/")
]


# Print the report heading.
print("===== CloudPulse Health Report =====")

# Check each website and print its report.
for service in services:
    result = service.check_health()

    print("Service:", result["name"])
    print("URL:", result["url"])
    print("HTTP Status Code:", result["status_code"])
    print("Health:", result["health"])
    print("Response Time:", result["response_time_ms"], "ms")
    print("Performance:", result["performance"])

    if result["error"]:
        print("Error:", result["error"])

    print("------------------------------")
