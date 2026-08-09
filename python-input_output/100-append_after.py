#!/usr/bin/python3
"""
This module contains a function that inserts text after
each line containing a specific string.
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Insert new_string after each line containing search_string.
    """
    with open(filename, "r", encoding="utf-8") as file:
        lines = file.readlines()

    with open(filename, "w", encoding="utf-8") as file:
        for line in lines:
            file.write(line)

            if search_string in line:
                file.write(new_string)
