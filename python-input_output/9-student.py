#!/usr/bin/python3
"""
This module defines a Student class.
"""


class Student:
    """Student class."""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Return the dictionary representation of the Student.

        If attrs is a list of strings, return only the attributes
        whose names are contained in attrs.
        """
        if isinstance(attrs, list):
            return {
                key: self.__dict__[key]
                for key in attrs
                if key in self.__dict__
            }

        return self.__dict__
