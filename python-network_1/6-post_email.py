#!/usr/bin/python3
"""Sends a POST request with an email parameter using requests."""

import requests
import sys


def main():
    """Send POST request and display the response body."""
    url = sys.argv[1]
    email = sys.argv[2]

    payload = {'email': email}
    response = requests.post(url, data=payload)

    print(response.text)


if __name__ == "__main__":
    main()
