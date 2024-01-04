#!/usr/bin/python3
"""Module 2-rectangle
Defines a class Rectangle
"""



class Rectangle:
    """Defines a class rectangle by private instance
    attributes width and height with public instance
    method area and perimeter.
    """

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
        """Retrieves the width"""
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
        """Retrieves the height"""
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
        """Calculates the area of the rectangle instance
        Returns:
            Area of the rectangle, given by width * height.
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
