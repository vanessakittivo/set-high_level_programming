cat > 2-post_email.py << 'EOF'
#!/usr/bin/python3
"""
This script sends a POST request with an email parameter and displays the response.
"""

import urllib.request
import urllib.parse
import sys


def main():
    """Send POST request with email and display response."""
    url = sys.argv[1]
    email = sys.argv[2]
    
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    
    with urllib.request.urlopen(url, data) as response:
        print(response.read().decode('utf-8'))


if __name__ == "__main__":
    main()
EOF

chmod +x 2-post_email.py
