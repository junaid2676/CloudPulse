
# Project: CloudPulse
# Purpose: Check the health of multiple real websites.

# Import requests to send HTTP requests.
import requests


# Check one website and return its health information.
def check_service(service_name, url):
    try:
        # Send a request and wait at most 5 seconds.
        response = requests.get(url, timeout=5)

        # Get the HTTP status code.
        status_code = response.status_code

        # Decide whether the website is healthy.
        if 200 <= status_code < 300:
            health_status = "HEALTHY"
        else:
            health_status = "UNHEALTHY"

        # Return the results to the code that called this function.
        return service_name, url, status_code, health_status

    except requests.RequestException:
        # Return UNREACHABLE if the request fails.
        return service_name, url, None, "UNREACHABLE"


# Store the services we want to check.
services = [
    {"name": "Example Website", "url": "https://example.com"},
    {"name": "Python Website", "url": "https://www.python.org"},
    {"name": "GitHub", "url": "https://github.com"},
    {"name": "Nonexistent Website", "url": "https://nonexistentwebsite.example.com"}
]


# Print the report heading.
print("===== CloudPulse Health Report =====")

# Check each service using our function.
for service in services:
    # Pass the service name and URL into the function.
    result = check_service(service["name"], service["url"])

    # Unpack the four values returned by the function.
    service_name, url, status_code, health_status = result

    # Print the report.
    print("Service:", service_name)
    print("URL:", url)
    print("HTTP Status Code:", status_code)
    print("Health:", health_status)
    print("------------------------------")