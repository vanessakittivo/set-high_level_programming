#!/usr/bin/python3
"""
This module provides a function to find a peak in a list of unsorted integers.
"""


def find_peak(list_of_integers):
    """
    Find a peak element in a list of unsorted integers.

    A peak element is greater than or equal to its neighbors.

    Args:
        list_of_integers (list): List of integers

    Returns:
        int or None: A peak element, or None if the list is empty

    Complexity:
        O(log n) time, O(1) space

    Example:
        >>> find_peak([1, 2, 4, 6, 3])
        6
        >>> find_peak([4, 2, 1, 2, 3, 1])
        4
    """
    if not list_of_integers:
        return None

    left = 0
    right = len(list_of_integers) - 1

    while left < right:
        mid = (left + right) // 2

        if list_of_integers[mid] < list_of_integers[mid + 1]:
            left = mid + 1
        else:
            right = mid

    return list_of_integers[left]
