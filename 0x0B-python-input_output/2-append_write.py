#!/usr/bin/python3
"""Module 2-append_write.py
appends a string at the end of a text file
"""


def append_write(filename="", text=""):
    """appends a string at the end of a text file
    and returns the number of characters added.

    Args:
       - filename: name of the file
       - text: text to be appended.
    Return:
       number of characters added.
    """

    with open(filename, mode='a+') as myfile:
        return myfile.write(text)
