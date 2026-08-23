#!/usr/bin/python3
"""Handles HTTP errors using urllib."""

import urllib.request
import urllib.error
import sys


def main():
    """Send request and display body or error code."""
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")


if __name__ == "__main__":
    main()
