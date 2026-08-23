#!/usr/bin/python3
"""Handles HTTP errors using requests."""

import requests
import sys


def main():
    """Send request and display body or error code."""
    url = sys.argv[1]

    response = requests.get(url)

    if response.status_code >= 400:
        print(f"Error code: {response.status_code}")
    else:
        print(response.text)


if __name__ == "__main__":
    main()
