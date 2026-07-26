#!/usr/bin/python3
"""Defines a LockedClass."""


class LockedClass:
    """Prevent the user from dynamically creating new attributes."""

    __slots__ = ["first_name"]
