cat > 0-hbtn_status.py << 'EOF'
#!/usr/bin/python3
"""
This script fetches https://alx-intranet.hbtn.io/status using urllib.
"""

import urllib.request


def main():
    """Fetch and display status response."""
    url = 'https://alx-intranet.hbtn.io/status'
    
    with urllib.request.urlopen(url) as response:
        content = response.read()
        
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content.decode('utf-8')))


if __name__ == "__main__":
    main()
EOF

chmod +x 0-hbtn_status.py
