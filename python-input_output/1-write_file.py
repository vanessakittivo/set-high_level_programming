#!/usr/bin/python3
"""
This module provides a function to write text to a file.
"""


def write_file(filename="", text=""):
    """
    Write a string to a text file (UTF8) and return
    the number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
