#!/usr/bin/python3
"""Takes GitHub credentials and displays the user id using the GitHub API."""

import requests
import sys


def main():
    """Fetch and display GitHub user id."""
    if len(sys.argv) != 3:
        print("Usage: ./10-my_github.py <username> <token>")
        sys.exit(1)

    username = sys.argv[1]
    token = sys.argv[2]

    url = "https://api.github.com/user"

    try:
        response = requests.get(url, auth=(username, token))

        if response.status_code == 200:
            user_data = response.json()
            print(user_data.get('id'))
        else:
            print(None)

    except requests.exceptions.RequestException:
        print(None)


if __name__ == "__main__":
    main()
