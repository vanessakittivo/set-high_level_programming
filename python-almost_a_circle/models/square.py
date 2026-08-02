#!/usr/bin/python3
"""This module defines the Square class."""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a Square."""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get the size."""
        return self.width

    @size.setter
    def size(self, value):
        """Set the size."""
        self.width = value
        self.height = value

    def __str__(self):
        """Return the string representation of the Square."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id,
            self.x,
            self.y,
            self.size
        )

    def update(self, *args, **kwargs):
        """Assign attributes."""
        attrs = ["id", "size", "x", "y"]

        if len(args) != 0:
            for i, value in enumerate(args):
                if i >= len(attrs):
                    break
                setattr(self, attrs[i], value)
        else:
            for key, value in kwargs.items():
                if key in attrs:
                    setattr(self, key, value)

    def to_dictionary(self):
        """Return the dictionary representation of a Square."""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
