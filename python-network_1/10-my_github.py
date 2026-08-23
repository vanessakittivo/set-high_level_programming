cat > 10-my_github.py << 'EOF'
#!/usr/bin/python3
"""
This script takes GitHub credentials and uses the GitHub API to display the user id.
"""

import requests
import sys


def main():
    """Fetch and display GitHub user id."""
    username = sys.argv[1]
    token = sys.argv[2]
    
    url = 'https://api.github.com/user'
    
    response = requests.get(url, auth=(username, token))
    
    if response.status_code == 200:
        user_data = response.json()
        print(user_data.get('id'))
    else:
        print(None)


if __name__ == "__main__":
    main()
EOF

chmod +x 10-my_github.py
