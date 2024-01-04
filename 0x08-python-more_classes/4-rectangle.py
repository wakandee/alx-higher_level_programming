#!/usr/bin/python3
"""Module 4-rectangle
Defines a class Rectangle
"""



class Rectangle:
    """Defines a class rectangle by width and height"""

    def __init__(self, width=0, height=0):
        """Initialized Rectangle instance
        Args:
            width: width of the rectangle
            height: height of the rctangle
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Retrieves the width of the rectangle instance"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the width of the rectangle instance.
        Args:
           value: value of the width must be an integer.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the height of the rectangle instance"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the height of the rectangle instance.
        Args:
           value: value of the height must be an integer.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates the area of a Rectangle instance
        Returns:
            area of the rectangle, given by height * width
        """
        return self.__width * self.__height

    def perimeter(self):
        """Calculates the perimeter of a Rectangle instance
        Returns:
            Perimeter of the rectangle, given by 2 * (height + width)
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """Return an informal and nicely printable string representation
        of a rectangle instance, filled with the '#' characters."""
        if self.__width == 0 or self.__height == 0:
            return ''
        rec_str = ''
        for i in range(self.height):
            for j in range(self.width):
                rec_str += '#'
            rec_str += '\n'
        return rec_str[:-1]

    def __repr__(self):
        """Return a string representation of a Rectangle instance
        that is able to recreate a new instance using eval().
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)
