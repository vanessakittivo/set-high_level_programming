#!/usr/bin/python3
"""Adds 2 integers."""


def add_integer(a, b=98):
    """Return the addition of two integers.

    Args:
        a: The first integer or float.
        b: The second integer or float, defaulting to 98.

    Returns:
        The integer result of a + b.

    Raises:
        TypeError: If a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
