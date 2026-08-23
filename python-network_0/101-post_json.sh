#!/bin/bash
# This script sends a JSON POST request with the contents of a file and displays the body
curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1"
