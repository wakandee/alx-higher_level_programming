#!/usr/bin/python3
"""Module 3-to_json_string.py
returns the JSON representation of an object
"""


import json


def to_json_string(my_obj):
    """ returns the JSON representation of an object

    Args:
       - my_obj: object to print its json representation.

    Return: json representation
    """

    return json.dumps(my_obj)
