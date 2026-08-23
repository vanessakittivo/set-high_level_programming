#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status using requests."""

import requests


def main():
    """Display the response body with type and content."""
    url = 'https://alx-intranet.hbtn.io/status'

    response = requests.get(url)

    print("Body response:")
    print(f"\t- type: {type(response.text)}")
    print(f"\t- content: {response.text}")


if __name__ == "__main__":
    main()
