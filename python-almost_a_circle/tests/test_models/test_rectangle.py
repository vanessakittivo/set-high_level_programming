#!/usr/bin/python3
"""Unit tests for models.rectangle"""

import io
import os
import unittest
from contextlib import redirect_stdout

from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Tests for Rectangle class."""

    def setUp(self):
        """Reset Base ids before every test."""
        Base._Base__nb_objects = 0
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")

    # ---------- Constructor ----------

    def test_rectangle_ids(self):
        r1 = Rectangle(1, 2)
        r2 = Rectangle(3, 4)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 2)

    def test_manual_id(self):
        r = Rectangle(1, 2, 0, 0, 89)
        self.assertEqual(r.id, 89)

    def test_width(self):
        r = Rectangle(5, 2)
        self.assertEqual(r.width, 5)

    def test_height(self):
        r = Rectangle(5, 7)
        self.assertEqual(r.height, 7)

    def test_x(self):
        r = Rectangle(5, 7, 3)
        self.assertEqual(r.x, 3)

    def test_y(self):
        r = Rectangle(5, 7, 3, 8)
        self.assertEqual(r.y, 8)

    # ---------- Type validation ----------

    def test_width_string(self):
        with self.assertRaises(TypeError):
            Rectangle("1", 2)

    def test_height_string(self):
        with self.assertRaises(TypeError):
            Rectangle(1, "2")

    def test_x_string(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3")

    def test_y_string(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "4")

    def test_width_float(self):
        with self.assertRaises(TypeError):
            Rectangle(1.5, 2)

    def test_height_float(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2.5)

    def test_x_float(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3.5)

    def test_y_float(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4.5)

    # ---------- Value validation ----------

    def test_width_zero(self):
        with self.assertRaises(ValueError):
            Rectangle(0, 2)

    def test_height_zero(self):
        with self.assertRaises(ValueError):
            Rectangle(2, 0)

    def test_width_negative(self):
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)

    def test_height_negative(self):
        with self.assertRaises(ValueError):
            Rectangle(1, -2)

    def test_x_negative(self):
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -1)

    def test_y_negative(self):
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 0, -1)

    # ---------- area() ----------

    def test_area(self):
        """Test area()."""
        r = Rectangle(3, 4)
        self.assertEqual(r.area(), 12)

    def test_area_square(self):
        """Test area of square-shaped rectangle."""
        r = Rectangle(5, 5)
        self.assertEqual(r.area(), 25)

    # ---------- __str__() ----------

    def test_str(self):
        """Test __str__()."""
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

    def test_str_default(self):
        """Test __str__() with default x and y."""
        r = Rectangle(2, 3, 0, 0, 99)
        self.assertEqual(str(r), "[Rectangle] (99) 0/0 - 2/3")

    # ---------- display() ----------

    def test_display(self):
        """Test display()."""
        r = Rectangle(2, 3)

        output = io.StringIO()

        with redirect_stdout(output):
            r.display()

        self.assertEqual(
            output.getvalue(),
            "##\n"
            "##\n"
            "##\n"
        )

    def test_display_x(self):
        """Test display() with x."""
        r = Rectangle(2, 2, 2)

        output = io.StringIO()

        with redirect_stdout(output):
            r.display()

        self.assertEqual(
            output.getvalue(),
            "  ##\n"
            "  ##\n"
        )

    def test_display_y(self):
        """Test display() with y."""
        r = Rectangle(2, 2, 0, 2)

        output = io.StringIO()

        with redirect_stdout(output):
            r.display()

        self.assertEqual(
            output.getvalue(),
            "\n\n"
            "##\n"
            "##\n"
        )

    def test_display_x_y(self):
        """Test display() with x and y."""
        r = Rectangle(2, 2, 2, 1)

        output = io.StringIO()

        with redirect_stdout(output):
            r.display()

        self.assertEqual(
            output.getvalue(),
            "\n"
            "  ##\n"
            "  ##\n"
        )

    # ---------- update(*args) ----------

    def test_update_id(self):
        """Test update(id)."""
        r = Rectangle(10, 10, 10, 10)
        r.update(89)
        self.assertEqual(r.id, 89)

    def test_update_id_width(self):
        """Test update(id, width)."""
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 1)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 1)

    def test_update_id_width_height(self):
        """Test update(id, width, height)."""
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 1, 2)
        self.assertEqual((r.id, r.width, r.height), (89, 1, 2))

    def test_update_id_width_height_x(self):
        """Test update(id, width, height, x)."""
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 1, 2, 3)
        self.assertEqual((r.id, r.width, r.height, r.x), (89, 1, 2, 3))

    def test_update_all_args(self):
        """Test update(id, width, height, x, y)."""
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 1, 2, 3, 4)
        self.assertEqual(
            (r.id, r.width, r.height, r.x, r.y),
            (89, 1, 2, 3, 4)
        )

    # ---------- update(**kwargs) ----------

    def test_update_kwargs_id(self):
        """Test update(id=89)."""
        r = Rectangle(10, 10)
        r.update(id=89)
        self.assertEqual(r.id, 89)

    def test_update_kwargs_width(self):
        """Test update(width=7)."""
        r = Rectangle(10, 10)
        r.update(width=7)
        self.assertEqual(r.width, 7)

    def test_update_kwargs_height(self):
        """Test update(height=9)."""
        r = Rectangle(10, 10)
        r.update(height=9)
        self.assertEqual(r.height, 9)

    def test_update_kwargs_x(self):
        """Test update(x=5)."""
        r = Rectangle(10, 10)
        r.update(x=5)
        self.assertEqual(r.x, 5)

    def test_update_kwargs_y(self):
        """Test update(y=8)."""
        r = Rectangle(10, 10)
        r.update(y=8)
        self.assertEqual(r.y, 8)

    def test_update_kwargs_all(self):
        """Test update(**kwargs)."""
        r = Rectangle(10, 10)
        r.update(id=89, width=1, height=2, x=3, y=4)

        self.assertEqual(
            (r.id, r.width, r.height, r.x, r.y),
            (89, 1, 2, 3, 4)
        )

    # ---------- to_dictionary() ----------

    def test_to_dictionary(self):
        """Test to_dictionary()."""
        r = Rectangle(10, 2, 1, 9, 7)

        expected = {
            "id": 7,
            "width": 10,
            "height": 2,
            "x": 1,
            "y": 9
        }

        self.assertEqual(r.to_dictionary(), expected)

    def test_to_dictionary_type(self):
        """Dictionary returned should be dict."""
        r = Rectangle(1, 2)
        self.assertIsInstance(r.to_dictionary(), dict)

    # ---------- create() ----------

    def test_create(self):
        """Test Rectangle.create()."""
        r = Rectangle.create(
            **{
                "id": 89,
                "width": 10,
                "height": 5,
                "x": 1,
                "y": 2
            }
        )

        self.assertIsInstance(r, Rectangle)
        self.assertEqual(
            (r.id, r.width, r.height, r.x, r.y),
            (89, 10, 5, 1, 2)
        )

    def test_create_returns_new_instance(self):
        """create() should return a new object."""
        r1 = Rectangle(3, 5, 1)
        r2 = Rectangle.create(**r1.to_dictionary())

        self.assertFalse(r1 is r2)
        self.assertEqual(r1.to_dictionary(), r2.to_dictionary())

    # ---------- save_to_file() ----------

    def test_save_to_file_none(self):
        """Test save_to_file(None)."""
        Rectangle.save_to_file(None)

        self.assertTrue(os.path.exists("Rectangle.json"))

        with open("Rectangle.json", "r", encoding="utf-8") as file:
            self.assertEqual(file.read(), "[]")

    def test_save_to_file_empty(self):
        """Test save_to_file([])."""
        Rectangle.save_to_file([])

        with open("Rectangle.json", "r", encoding="utf-8") as file:
            self.assertEqual(file.read(), "[]")

    def test_save_to_file(self):
        """Test save_to_file([Rectangle])."""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)

        Rectangle.save_to_file([r1, r2])

        self.assertTrue(os.path.exists("Rectangle.json"))

    # ---------- load_from_file() ----------

    def test_load_from_file_no_file(self):
        """Test load_from_file() when file does not exist."""
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")

        self.assertEqual(Rectangle.load_from_file(), [])

    def test_load_from_file(self):
        """Test load_from_file()."""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)

        Rectangle.save_to_file([r1, r2])

        rectangles = Rectangle.load_from_file()

        self.assertEqual(len(rectangles), 2)
        self.assertIsInstance(rectangles[0], Rectangle)
        self.assertIsInstance(rectangles[1], Rectangle)

        self.assertFalse(rectangles[0] is r1)
        self.assertFalse(rectangles[1] is r2)

    def tearDown(self):
        """Delete generated files."""
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")


if __name__ == "__main__":
    unittest.main()
