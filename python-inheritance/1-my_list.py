#!/usr/bin/python3
"""Defines a MyList class that inherits from list."""


class MyList(list):
    """A list subclass with a method to print sorted values."""

    def print_sorted(self):
        """Print the list sorted in ascending order."""
        print(sorted(self))
