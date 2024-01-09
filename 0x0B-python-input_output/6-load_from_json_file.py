#!/usr/bin/python3
"""Module 6-load_from_json_file.py.
 creates an Object from a “JSON file”
"""


import json


def load_from_json_file(filename):
    """ creates an Object from a “JSON file”

    Args:
       - filename: name of the file.
    """

    with open(filename, 'r') as myfile:
        return json.load(myfile)
