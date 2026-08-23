cat > 8-json_api.py << 'EOF'
#!/usr/bin/python3
"""
This script sends a POST request with a letter and handles JSON response.
"""

import requests
import sys


def main():
    """Send POST request with letter and display JSON response."""
    url = 'http://0.0.0.0:5000/search_user'
    
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""
    
    payload = {'q': q}
    response = requests.post(url, data=payload)
    
    try:
        data = response.json()
        if data:
            print("[{}] {}".format(data.get('id'), data.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")


if __name__ == "__main__":
    main()
EOF

chmod +x 8-json_api.py
