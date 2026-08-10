#!/usr/bin/python3
"""Unittest for max_integer([..])"""

import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer."""

    def test_positive_numbers(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unsorted_list(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -2, -3]), -1)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([-5, 2, -1, 10, 3]), 10)

    def test_one_element(self):
        self.assertEqual(max_integer([7]), 7)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_same_values(self):
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)

    def test_maximum_first(self):
        self.assertEqual(max_integer([10, 3, 2, 1]), 10)

    def test_maximum_last(self):
        self.assertEqual(max_integer([1, 2, 3, 10]), 10)
