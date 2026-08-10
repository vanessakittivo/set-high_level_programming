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

    if not text:
        return

    lines = []
    current = ""
    skip_spaces = False

    for char in text:
        if skip_spaces and char == " ":
            continue

        skip_spaces = False

        if char in ".?:":
            current = current.rstrip()
            lines.append(current + char)
            current = ""
            skip_spaces = True
        else:
            current += char

    if current.strip():
        lines.append(current.strip())

    print("\n\n".join(lines))
