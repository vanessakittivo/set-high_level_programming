#!/usr/bin/python3
"""Defines a MyInt class with inverted equality operators."""


class MyInt(int):
    """MyInt class with inverted == and != operators."""

    def __eq__(self, other):
        """Invert the equality operator."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Invert the inequality operator."""
        return super().__eq__(other)
