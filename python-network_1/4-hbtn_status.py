cat > 4-hbtn_status.py << 'EOF'
#!/usr/bin/python3
"""
This script fetches https://alx-intranet.hbtn.io/status using requests.
"""

import requests


def main():
    """Fetch and display status response."""
    url = 'https://alx-intranet.hbtn.io/status'
    
    response = requests.get(url)
    
    print("Body response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))


if __name__ == "__main__":
    main()
EOF

chmod +x 4-hbtn_status.py
