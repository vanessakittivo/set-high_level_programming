#!/usr/bin/python3
"""Module for printing text with indentation."""


def text_indentation(text):
    """Print text with 2 new lines after '.', '?' and ':'.

    Args:
        text: The text to print.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    if text == "":
        return

    result = ""
    skip_spaces = False

    for char in text:
        if skip_spaces and char == " ":
            continue

        if char in ".?:":
            result += char
            result += "\n\n"
            skip_spaces = True
        else:
            result += char
            skip_spaces = False

    print(result.rstrip())
