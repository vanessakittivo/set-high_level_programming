#!/usr/bin/python3
"""
This module provides a function to load a Python object
from a JSON file.
"""

import json


def load_from_json_file(filename):
    """
    Create a Python object from the JSON representation
    stored in a file.
    """
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
