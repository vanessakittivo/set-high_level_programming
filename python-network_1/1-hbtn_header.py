cat > 1-hbtn_header.py << 'EOF'
#!/usr/bin/python3
"""
This script takes in a URL, sends a request, and displays the value of
X-Request-Id in the response header.
"""

import urllib.request
import sys


def main():
    """Fetch and display X-Request-Id header value."""
    url = sys.argv[1]
    
    with urllib.request.urlopen(url) as response:
        x_request_id = response.headers.get('X-Request-Id')
        print(x_request_id)


if __name__ == "__main__":
    main()
EOF

chmod +x 1-hbtn_header.py
