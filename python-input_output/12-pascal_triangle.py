#!/usr/bin/python3
"""
This module contains a function that creates Pascal's triangle.
"""


def pascal_triangle(n):
    """
    Return a list of lists of integers representing Pascal's triangle
    of n.
    """
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        row = [1] * (i + 1)

        if i > 1:
            previous = triangle[i - 1]

            for j in range(1, i):
                row[j] = previous[j - 1] + previous[j]

        triangle.append(row)

    return triangle
