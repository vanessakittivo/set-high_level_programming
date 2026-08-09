#!/usr/bin/python3
"""
This module provides a function to read and print a text file.
"""


def read_file(filename=""):
    """
    Read a text file (UTF8) and print its content to stdout.
    """
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read(), end="")
