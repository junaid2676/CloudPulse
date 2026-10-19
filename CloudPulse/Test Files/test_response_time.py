
# Project: CloudPulse

import requests
import time


def check_service(service_name, url):
    try:
        # Record the time before sending the request
        start_time = time.perf_counter()

        # Send a request to the service
        response = requests.get(url, timeout=5)

        # Record the time after receiving the response
        end_time = time.perf_counter()

        # Calculate response time in milliseconds
        response_time_ms = (end_time - start_time) * 1000

        # Get the HTTP status code
        status_code = response.status_code

        # Check HTTP health
        if 200 <= status_code < 300:
            health_status = "HEALTHY"
        else:
            health_status = "UNHEALTHY"

        # Check performance separately from HTTP health
        if response_time_ms < 500:
            performance = "FAST"
        elif response_time_ms <= 1000:
            performance = "SLOW"
        else:
            performance = "VERY SLOW"

        # Return all results in a dictionary
        return {
            "name": service_name,
            "url": url,
            "status_code": status_code,
            "response_time_ms": round(response_time_ms, 2),
            "health": health_status,
            "performance": performance
        }

    except requests.RequestException as error:
        # Set a general explanation first
        error_message = (
            "Connection failed. Check the URL and network."
        )

        # Check whether the connection itself failed
        if isinstance(error, requests.exceptions.ConnectionError):
            error_message = (
                "Could not connect. Check the hostname, DNS, "
                "network connection, or server availability."
            )

        # Check whether the request took too long
        elif isinstance(error, requests.exceptions.Timeout):
            error_message = (
                "The service took too long to respond (timeout)."
            )

        # Return the results, including both error messages
        return {
            "name": service_name,
            "url": url,
            "status_code": None,
            "response_time_ms": None,
            "health": "UNREACHABLE",
            "performance": "UNKNOWN",
            "error": error_message,
            "technical_error": str(error)
        }


# Services that CloudPulse will monitor
services = [
    {
        "name": "Example Website",
        "url": "https://example.com"
    },
    {
        "name": "Python Website",
        "url": "https://www.python.org"
    },
    {
        "name": "GitHub",
        "url": "https://github.com"
    },
    {
        "name": "Nonexistent Website",
        "url": "https://nonexistentwebsite.example.com"
    },
    {
        "name": "Google",
        "url": "https://www.google.com"
    },
    {
        "name": "Slow Website",
        "url": "https://httpstat.us/200?sleep=2000"
    }
]


# Run the health checks and display the report
print("===== CloudPulse Health Report =====")

for service in services:
    result = check_service(service["name"], service["url"])

    print("Service:", result["name"])
    print("URL:", result["url"])
    print("HTTP Status Code:", result["status_code"])
    print("Response Time:", result["response_time_ms"], "ms")
    print("Health:", result["health"])
    print("Performance:", result["performance"])
                
    if "error" in result:
        print("Failure Reason:", result["error"])
        print("Technical Details:", result["technical_error"])
    else:
        print("Connection successful.")

    print("-----------------------------------")
 