import sys
from pathlib import Path
import requests
import time

# Find the CloudPulse project folder.
project_folder = Path(__file__).resolve().parent.parent

# Add Learning Main to Python's search path.
learning_main_folder = project_folder / "Learning Main"
sys.path.insert(0, str(learning_main_folder))

# Import the existing performance function.
from performance import classify_performance

class Service:
    def __init__(self, name, url):
        # Store information for this particular service.
        self.name = name
        self.url = url

    def check_health(self):
        # Start measuring how long the request takes.
        start_time = time.perf_counter()

        try:
            response = requests.get(self.url, timeout=5)

            # Convert elapsed time to milliseconds.
            elapsed_time = (time.perf_counter() - start_time) * 1000

            # Determine whether the website is healthy.
            if 200 <= response.status_code < 300:
                health = "HEALTHY"
            else:
                health = "UNHEALTHY"

            # Return all results together in a dictionary.
            return {
                "name": self.name,
                "url": self.url,
                "status_code": response.status_code,
                "response_time_ms": round(elapsed_time, 2),
                "health": health,
                "performance": classify_performance(elapsed_time),
                "error": None
            }

        except requests.RequestException as error:
            # Handle connection errors and timeouts without crashing.
            return {
                "name": self.name,
                "url": self.url,
                "status_code": None,
                "response_time_ms": None,
                "health": "UNREACHABLE",
                "performance": classify_performance(None),
                "error": str(error)
            }
