#!/usr/bin/python3
"""Module 0-read_file.py
creates a function that reads a text file.
"""


def read_file(filename=""):
    """a function that reads a text file(UTF8)
    and prints it to stdout.

    Args:
       - filename: name of the file
    """
    with open(filename) as myfile:
        read_text = myfile.read()
        print(read_text, end="")
