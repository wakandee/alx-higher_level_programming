#!/usr/bin/python3
"""
Module say_my_name
Prints first and last name

"""

def say_my_name(first_name, last_name=""):
    """prints My name is <first name> <last name>
    names must be strings otherwise, raise a TypeError,
    first_name must be a string or last_name must be a string.
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
