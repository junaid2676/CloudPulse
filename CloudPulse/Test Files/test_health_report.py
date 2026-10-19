
# Project: CloudPulse
# Complete service health and performance report

import requests
import time
from performance import classify_performance



    
def check_service(name, url):
    start_time = time.perf_counter()

    try:
        response = requests.get(url, timeout=3)
        end_time = time.perf_counter()

        response_time_ms = round(
            (end_time - start_time) * 1000, 2
        )
        status_code = response.status_code

        if 200 <= status_code < 300:
            health = "HEALTHY"
            error = None
        elif 300 <= status_code < 400:
            health = "REDIRECT"
            error = None
        else:
            health = "UNHEALTHY"
            error = "HTTP response indicates an issue."

    except requests.exceptions.Timeout:
        response_time_ms = None
        status_code = None
        health = "TIMEOUT"
        error = "The service took too long to respond."

    except requests.exceptions.ConnectionError:
        response_time_ms = None
        status_code = None
        health = "UNREACHABLE"
        error = "Could not connect to the service."

    performance = classify_performance(response_time_ms)

    return {
        "name": name,
        "url": url,
        "status_code": status_code,
        "response_time_ms": response_time_ms,
        "health": health,
        "performance": performance,
        "error": error
    }


services = [
    {"name": "Example", "url": "https://example.com"},
    {"name": "Python", "url": "https://www.python.org"},
    {
        "name": "Invalid Website",
        "url": "https://this-domain-should-not-exist-12345.example"
    }
]


print("========== CloudPulse Health Report ==========")

for service in services:
    result = check_service(service["name"], service["url"])

    print("Service:", result["name"])
    print("URL:", result["url"])
    print("Health:", result["health"])
    print("HTTP Status:", result["status_code"])
    print("Response Time:", result["response_time_ms"], "ms")
    print("Performance:", result["performance"])

    if result["error"] is not None:
        print("Error:", result["error"])

    print("---------------------------------------------")
    