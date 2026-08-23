#!/usr/bin/python3
"""Displays the value of X-Request-Id in the response header."""

import urllib.request
import sys


def main():
    """Get X-Request-Id header from URL response."""
    url = sys.argv[1]

    with urllib.request.urlopen(url) as response:
        x_request_id = response.headers.get('X-Request-Id')
        print(x_request_id)


if __name__ == "__main__":
    main()
