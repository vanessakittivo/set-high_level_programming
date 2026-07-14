#!/usr/bin/python3
def uniq_add(my_list=[]):
    """Add all unique integers in a list."""
    total = 0
    unique = []

    for num in my_list:
        if num not in unique:
            unique.append(num)
            total += num

    return total
