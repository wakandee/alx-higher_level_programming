#!/usr/bin/python3
"""Module 1-write_file.py.
writes a string to a text file.
"""


def write_file(filename="", text=""):
    """writes a string to a text file and
    returns the number of characters written.

    Args:
       - filename: name of the file.
       - text: string of text to write.
    Return:
         number of characters written.
    """

    with open(filename, mode='w+') as myfile:
        return myfile.write(text)
