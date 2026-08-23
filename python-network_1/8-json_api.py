#!/usr/bin/python3
"""Sends a POST request to search_user API with a letter."""

import requests
import sys


def main():
    """Handle search_user API requests with q parameter."""
    q = sys.argv[1] if len(sys.argv) > 1 else ""

    try:
        response = requests.post(
            "http://0.0.0.0:5000/search_user",
            data={'q': q}
        )

        if response.headers.get('content-type') != 'application/json':
            print("Not a valid JSON")
            return

        data = response.json()

        if data:
            print(f"[{data.get('id')}] {data.get('name')}")
        else:
            print("No result")

    except ValueError:
        print("Not a valid JSON")


if __name__ == "__main__":
    main()
