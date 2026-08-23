#!/bin/bash
# This script displays all HTTP methods accepted by the server
curl -s -I -X OPTIONS "$1" | grep -i "allow" | cut -d ' ' -f 2-
