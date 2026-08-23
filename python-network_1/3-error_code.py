cat > 3-error_code.py << 'EOF'
#!/usr/bin/python3
"""
This script sends a request to a URL and handles HTTP errors.
"""

import urllib.request
import urllib.error
import sys


def main():
    """Send request and handle HTTP errors."""
    url = sys.argv[1]
    
    try:
        with urllib.request.urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))


if __name__ == "__main__":
    main()
EOF

chmod +x 3-error_code.py
