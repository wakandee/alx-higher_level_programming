#!/usr/bin/python3
"""Module square.py
class Square that inherits from Rectangle.
"""

from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """a class Square that inherits from Rectangle.
    Public instance methods:
        - area()
        - display()
        - to_dictionary()
        - update()
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Initializing the Square instances

        Args:
            - __size: size
            - __x: position
            - __y: position
            - id: id
        """

        self.size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns a string representation of a Square instance."""

        s = "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)
        return s

    @property
    def size(self):
        """Retrieves the size of the Square instance."""

        return self.width

    @size.setter
    def size(self, value):
        """sets the size of the square to a value.

        Args:
            - value: value of the square must be an int.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
        self.__height = value

    def updates(self, *args, **kwargs):
        """Updates the attributes of the square.

        Args:
            - id attribute
            - size attribute
            - x attribute
            - y attribute
        """
        if args is not None and len(args) != 0:
            if len(args) >= 1:
                if type(args[0]) != int and args[0] is not None:
                    raise TypeError("id must be an integer")
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]

        else:
            for key, value in kwargs.items():
                if key == "id":
                    if type(value) != int and value is not None:
                        raise TypeError("id must be an integer")
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """Returns the dictionary representation of a Square."""

        my_dict = {'id': self.id, 'size': self.size,
                   'x': self.x, 'y': self.y}
        return my_dict
