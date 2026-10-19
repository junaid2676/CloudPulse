

# Project: CloudPulse
# Test different HTTP response types

import requests


def check_http_status(status_code):
    # Successful HTTP responses
    if 200 <= status_code < 300:
        return "HEALTHY", "The request succeeded."

    # Redirect responses
    elif 300 <= status_code < 400:
        return "REDIRECT", "The service redirected the request."

    # Client-side errors
    elif 400 <= status_code < 500:
        return "UNHEALTHY", "The request has a client-side HTTP error."

    # Server-side errors
    elif 500 <= status_code < 600:
        return "UNHEALTHY", "The server reported an error."

    # Unexpected status codes
    else:
        return "UNKNOWN", "Unexpected HTTP status code."


# Test several status codes without relying on external websites
test_status_codes = [200, 301, 404, 500, 503, 700]

print("===== CloudPulse HTTP Status Tests =====")

for code in test_status_codes:
    health, explanation = check_http_status(code)

    print("HTTP Status Code:", code)
    print("Health:", health)
    print("Explanation:", explanation)
    print("-----------------------------------")
