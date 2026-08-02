#!/usr/bin/python3
"""Unit tests for models.square"""

import os
import unittest

from models.base import Base
from models.square import Square


class TestSquare(unittest.TestCase):
    """Unit tests for Square class."""

    def setUp(self):
        """Reset Base counter and remove test file."""
        Base._Base__nb_objects = 0
        if os.path.exists("Square.json"):
            os.remove("Square.json")

    # ---------------- Constructor ----------------

    def test_square_exists(self):
        s = Square(5)
        self.assertIsInstance(s, Square)

    def test_square_x(self):
        s = Square(5, 2)
        self.assertEqual(s.x, 2)

    def test_square_x_y(self):
        s = Square(5, 2, 3)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)

    def test_square_id(self):
        s = Square(5, 2, 3, 89)
        self.assertEqual(s.id, 89)

    # ---------------- Type validation ----------------

    def test_size_string(self):
        with self.assertRaises(TypeError):
            Square("1")

    def test_x_string(self):
        with self.assertRaises(TypeError):
            Square(1, "2")

    def test_y_string(self):
        with self.assertRaises(TypeError):
            Square(1, 2, "3")

    # ---------------- Value validation ----------------

    def test_size_negative(self):
        with self.assertRaises(ValueError):
            Square(-1)

    def test_size_zero(self):
        with self.assertRaises(ValueError):
            Square(0)

    def test_x_negative(self):
        with self.assertRaises(ValueError):
            Square(1, -2)

    def test_y_negative(self):
        with self.assertRaises(ValueError):
            Square(1, 2, -3)

    # ---------------- Size property ----------------

    def test_size_property(self):
        s = Square(5)
        self.assertEqual(s.size, 5)

    def test_size_setter(self):
        s = Square(5)
        s.size = 10
        self.assertEqual(s.size, 10)

    # ---------------- Area ----------------

    def test_area(self):
        s = Square(4)
        self.assertEqual(s.area(), 16)

    # ---------------- __str__ ----------------

    def test_str(self):
        s = Square(5, 2, 1, 12)
        self.assertEqual(str(s), "[Square] (12) 2/1 - 5")

    # ---------------- update(*args) ----------------

    def test_update_id(self):
        s = Square(5)
        s.update(89)
        self.assertEqual(s.id, 89)

    def test_update_size(self):
        s = Square(5)
        s.update(89, 10)
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 10)

    def test_update_x(self):
        s = Square(5)
        s.update(89, 10, 3)
        self.assertEqual((s.id, s.size, s.x), (89, 10, 3))

    def test_update_all_args(self):
        s = Square(5)
        s.update(89, 10, 3, 4)
        self.assertEqual((s.id, s.size, s.x, s.y), (89, 10, 3, 4))

    # ---------------- update(**kwargs) ----------------

    def test_update_kwargs(self):
        s = Square(5)
        s.update(id=99, size=7, x=2, y=1)
        self.assertEqual((s.id, s.size, s.x, s.y), (99, 7, 2, 1))

    # ---------------- to_dictionary ----------------

    def test_to_dictionary(self):
        s = Square(10, 2, 1, 9)
        expected = {
            "id": 9,
            "size": 10,
            "x": 2,
            "y": 1
        }
        self.assertEqual(s.to_dictionary(), expected)

    def test_dictionary_type(self):
        s = Square(3)
        self.assertIsInstance(s.to_dictionary(), dict)

    # ---------------- create ----------------

    def test_create(self):
        s = Square.create(
            **{
                "id": 89,
                "size": 6,
                "x": 3,
                "y": 4
            }
        )

        self.assertIsInstance(s, Square)
        self.assertEqual((s.id, s.size, s.x, s.y), (89, 6, 3, 4))

    # ---------------- save_to_file ----------------

    def test_save_to_file_none(self):
        """Test Square.save_to_file(None)."""
        Square.save_to_file(None)

        self.assertTrue(os.path.exists("Square.json"))

        with open("Square.json", "r", encoding="utf-8") as file:
            self.assertEqual(file.read(), "[]")

    def test_save_to_file_empty_list(self):
        """Test Square.save_to_file([])."""
        Square.save_to_file([])

        self.assertTrue(os.path.exists("Square.json"))

        with open("Square.json", "r", encoding="utf-8") as file:
            self.assertEqual(file.read(), "[]")

    def test_save_to_file_one_square(self):
        """Test Square.save_to_file([Square(1)])."""
        s = Square(1)

        Square.save_to_file([s])

        self.assertTrue(os.path.exists("Square.json"))

        with open("Square.json", "r", encoding="utf-8") as file:
            self.assertNotEqual(file.read(), "")

    # ---------------- load_from_file ----------------

    def test_load_no_file(self):
        if os.path.exists("Square.json"):
            os.remove("Square.json")

        self.assertEqual(Square.load_from_file(), [])

    def test_load_file(self):
        s1 = Square(5)
        s2 = Square(7, 2, 1)

        Square.save_to_file([s1, s2])

        squares = Square.load_from_file()

        self.assertEqual(len(squares), 2)
        self.assertIsInstance(squares[0], Square)
        self.assertIsInstance(squares[1], Square)

    def tearDown(self):
        """Remove generated files."""
        if os.path.exists("Square.json"):
            os.remove("Square.json")


if __name__ == "__main__":
    unittest.main()
