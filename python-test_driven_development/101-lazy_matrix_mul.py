#!/usr/bin/python3
"""
Module for lazy matrix multiplication
"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiply two matrices using NumPy.
    """

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")

    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")

    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if len(m_a) == 0 or any(len(row) == 0 for row in m_a):
        raise ValueError("m_a can't be empty")

    if len(m_b) == 0 or any(len(row) == 0 for row in m_b):
        raise ValueError("m_b can't be empty")

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

    size_a = len(m_a[0])
    for row in m_a:
        if len(row) != size_a:
            raise TypeError(
                "each row of m_a must should be of the same size"
            )

    size_b = len(m_b[0])
    for row in m_b:
        if len(row) != size_b:
            raise TypeError(
                "each row of m_b must should be of the same size"
            )

    if size_a != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    return np.matmul(m_a, m_b)
