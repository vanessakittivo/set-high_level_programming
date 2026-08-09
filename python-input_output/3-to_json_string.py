#!/usr/bin/python3
"""
This module provides a function to convert a Python object
to a JSON string.
"""

import json


def to_json_string(my_obj):
    """
    Return the JSON representation of an object.
    """
    return json.dumps(my_obj)
