    
# Project: CloudPulse
# Test connection failures and timeouts

import requests


def check_connection(url):
    try:
        response = requests.get(url, timeout=3)

        return {
            "health": "RESPONDING",
            "status_code": response.status_code,
            "error": None
        }

    except requests.exceptions.Timeout:
        return {
            "health": "TIMEOUT",
            "status_code": None,
            "error": "The service took too long to respond."
        }

    except requests.exceptions.ConnectionError:
        return {
            "health": "UNREACHABLE",
            "status_code": None,
            "error": "Could not connect to the service."
        }


# Test 1: A website that should respond
result = check_connection("https://example.com")
print("Working website:", result)

# Test 2: A hostname that should not exist
result = check_connection(
    "https://this-domain-should-not-exist-12345.example"
)
print("Invalid hostname:", result)

