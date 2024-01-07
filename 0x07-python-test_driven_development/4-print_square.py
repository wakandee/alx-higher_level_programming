#!/usr/bin/python3
"""
Module print_square
Prints a square with character #
"""

def print_square(size):
    """prints a square with the character #.
    where size is the length and width of square.
    """

    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size < 0 and float:
        raise TypeError("size must be an integer")

    for i in range(size):
        for j in range(size):
            print('#', end='')
        print()
