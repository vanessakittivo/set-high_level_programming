#!/usr/bin/python3
"""Unit tests for models/base.py"""

import os
import unittest

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Tests for the Base class."""

    def setUp(self):
        """Reset the object counter before each test."""
        Base._Base__nb_objects = 0

        if os.path.exists("Base.json"):
            os.remove("Base.json")

        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")

        if os.path.exists("Square.json"):
            os.remove("Square.json")

    def test_auto_id(self):
        """Test automatic id assignment."""
        b1 = Base()
        b2 = Base()

        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_manual_id(self):
        """Test manual id."""
        b = Base(89)
        self.assertEqual(b.id, 89)

    def test_to_json_string_none(self):
        """Test None."""
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_empty(self):
        """Test empty list."""
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string(self):
        """Test JSON conversion."""
        dictionary = [{"id": 12}]
        result = Base.to_json_string(dictionary)

        self.assertIsInstance(result, str)
        self.assertEqual(result, '[{"id": 12}]')

    def test_from_json_none(self):
        """Test None."""
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_empty(self):
        """Test empty string."""
        self.assertEqual(Base.from_json_string(""), [])

    def test_from_json(self):
        """Test JSON decoding."""
        result = Base.from_json_string('[{"id": 89}]')

        self.assertIsInstance(result, list)
        self.assertEqual(result[0]["id"], 89)

    def test_save_none_rectangle(self):
        """Test save None."""
        Rectangle.save_to_file(None)

        self.assertTrue(os.path.exists("Rectangle.json"))

    def test_load_file_not_exist(self):
        """Test loading nonexistent file."""
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")

        self.assertEqual(Rectangle.load_from_file(), [])

    def test_create_rectangle(self):
        """Test Rectangle.create."""
        r = Rectangle.create(
            **{
                "id": 89,
                "width": 10,
                "height": 5,
                "x": 1,
                "y": 2
            }
        )

        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 5)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 2)

    def test_create_square(self):
        """Test Square.create."""
        s = Square.create(
            **{
                "id": 5,
                "size": 7,
                "x": 3,
                "y": 4
            }
        )

        self.assertEqual(s.id, 5)
        self.assertEqual(s.size, 7)
        self.assertEqual(s.x, 3)
        self.assertEqual(s.y, 4)


if __name__ == "__main__":
    unittest.main()
