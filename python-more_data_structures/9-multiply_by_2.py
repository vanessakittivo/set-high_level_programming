#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """Return a new dictionary with all values multiplied by 2."""
    new_dictionary = {}

    for key in a_dictionary:
        new_dictionary[key] = a_dictionary[key] * 2

    return new_dictionary
