#!/usr/bin/python3
"""
This module provides a function to save a Python object
to a JSON file.
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Write the JSON representation of my_obj to a file.
    """
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)
