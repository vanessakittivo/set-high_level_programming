cat > 7-error_code.py << 'EOF'
#!/usr/bin/python3
"""
This script sends a request and handles HTTP errors using requests.
"""

import requests
import sys


def main():
    """Send request and handle HTTP errors."""
    url = sys.argv[1]
    
    response = requests.get(url)
    
    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)


if __name__ == "__main__":
    main()
EOF

chmod +x 7-error_code.py
