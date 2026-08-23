#!/usr/bin/python3
"""
Lists the 10 most recent commits of a repository using the GitHub API.
"""

import requests
import sys


def main():
    """Fetch and display the 10 most recent commits."""
    if len(sys.argv) != 3:
        print("Usage: ./100-github_commits.py <repository> <owner>")
        sys.exit(1)

    repo = sys.argv[1]
    owner = sys.argv[2]
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"

    try:
        response = requests.get(url, params={'per_page': 10})
        response.raise_for_status()

        for commit in response.json():
            sha = commit.get('sha')
            author = commit.get('commit', {}).get('author', {})
            name = author.get('name', 'Unknown')
            print(f"{sha}: {name}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
