#!/usr/bin/python3
"""Module for multiplying two matrices."""


def matrix_mul(m_a, m_b):
    """Multiply two matrices."""

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")

    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")

    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    for row in m_a:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(
                    "m_a should contain only integers or floats"
                )

    for row in m_b:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(
                    "m_b should contain only integers or floats"
                )

    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError(
            "each row of m_a must should be of the same size"
        )

    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError(
            "each row of m_b must should be of the same size"
        )

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = []

    for i in range(len(m_a)):
        row = []
        for j in range(len(m_b[0])):
            total = 0
            for k in range(len(m_b)):
                total += m_a[i][k] * m_b[k][j]
            row.append(total)
        result.append(row)

    return result
