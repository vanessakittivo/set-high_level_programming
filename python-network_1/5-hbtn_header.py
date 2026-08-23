#!/usr/bin/python3
"""Displays X-Request-Id header using requests."""

import requests
import sys


def main():
    """Get X-Request-Id header from URL response."""
    url = sys.argv[1]

    response = requests.get(url)
    x_request_id = response.headers.get('X-Request-Id')
    print(x_request_id)


if __name__ == "__main__":
    main()
