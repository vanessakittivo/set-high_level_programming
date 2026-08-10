#!/usr/bin/python3
"""Module for matrix multiplication."""


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

    if not m_a or not m_a[0]:
        raise ValueError("m_a can't be empty")

    if not m_b or not m_b[0]:
        raise ValueError("m_b can't be empty")

    for row in m_a:
        for value in row:
            if not isinstance(value, (int, float)):
                raise TypeError(
                    "m_a should contain only integers or floats"
                )

    for row in m_b:
        for value in row:
            if not isinstance(value, (int, float)):
                raise TypeError(
                    "m_b should contain only integers or floats"
                )

    m_a_size = len(m_a[0])
    for row in m_a:
        if len(row) != m_a_size:
            raise TypeError(
                "each row of m_a must be of the same size"
            )

    m_b_size = len(m_b[0])
    for row in m_b:
        if len(row) != m_b_size:
            raise TypeError(
                "each row of m_b must be of the same size"
            )

    if m_a_size != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = []

    for i in range(len(m_a)):
        row = []
        for j in range(m_b_size):
            total = 0
            for k in range(m_a_size):
                total += m_a[i][k] * m_b[k][j]
            row.append(total)
        result.append(row)

    return result
