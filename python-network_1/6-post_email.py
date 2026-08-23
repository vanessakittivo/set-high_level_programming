cat > 6-post_email.py << 'EOF'
#!/usr/bin/python3
"""
This script sends a POST request with an email parameter using requests.
"""

import requests
import sys


def main():
    """Send POST request with email and display response."""
    url = sys.argv[1]
    email = sys.argv[2]
    
    payload = {'email': email}
    response = requests.post(url, data=payload)
    
    print(response.text)


if __name__ == "__main__":
    main()
EOF

chmod +x 6-post_email.py
