#!/usr/bin/python3
"""Defines a function that adds an attribute to an object."""


def add_attribute(obj, name, value):
    """Add a new attribute if the object allows it."""
    if hasattr(obj, "__dict__"):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
