#!/usr/bin/python3
"""Module 7-base_geometry.py
a class BaseGeometry with public instance methods
"""


class BaseGeometry():
    """a class BaseGeometry with public instance methods."""

    def area(self):
        """public instance that raises an Exception with the message
        'area() is not implemented'."""

    def integer_validator(self, name, value):
        """public instance that validates value.
        if value is not an integer:
         raise a TypeError exception, with the message <name> must be an integer
        if value is less or equal to 0:
         raise a ValueError exception with the message <name> must
         be greater than 0

        Args:
           name: a string.
           value: value to validate.
        """

        self.name = name
        self.value = value

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value < 0 or value == 0:
            raise ValueError("{} must be greater than 0".format(name))
