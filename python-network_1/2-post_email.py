#!/usr/bin/python3
"""Sends a POST request with an email parameter using urllib."""

import urllib.request
import urllib.parse
import sys


def main():
    """Send POST request and display the response body."""
    url = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({'email': email}).encode('utf-8')

    with urllib.request.urlopen(url, data) as response:
        print(response.read().decode('utf-8'))


if __name__ == "__main__":
    main()
