cat > 100-github_commits.py << 'EOF'
#!/usr/bin/python3
"""
This script lists 10 commits (from most recent to oldest) of a repository.
"""

import requests
import sys


def main():
    """Fetch and display the 10 most recent commits."""
    repo = sys.argv[1]
    owner = sys.argv[2]
    
    url = 'https://api.github.com/repos/{}/{}/commits'.format(owner, repo)
    
    response = requests.get(url, params={'per_page': 10})
    
    commits = response.json()
    
    for commit in commits:
        sha = commit.get('sha')
        author = commit.get('commit').get('author').get('name')
        print("{}: {}".format(sha, author))


if __name__ == "__main__":
    main()
EOF

chmod +x 100-github_commits.py
