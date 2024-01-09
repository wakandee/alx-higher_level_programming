#!/usr/bin/python3
"""Module 4-from_json_string.py
returns an object (Python data structure)
represented by a JSON string
"""

import json


def from_json_string(my_str):
    """returns an object (Python data structure)
    represented by a JSON string.

    Args:
       - my_str: the json string to return its object.

    Return: an object (Python data structure) represented by a JSON string
    """

    return json.loads(my_str)
