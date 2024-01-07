#!/usr/bin/python3
"""
Module text_indentation
Prints a text with 2 new lines after
a set of characters
"""

def text_indentation(text):
    """prints a text with 2 new lines
    after each of these characters:
    {'.', '?' and ':'}
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    for char in ".?:":
        text = (char + "\n\n").join(
            [line.strip(" ") for line in text.split(char)])
        print("{}".format(text), end='')
