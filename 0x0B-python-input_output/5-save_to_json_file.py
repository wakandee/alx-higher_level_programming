#!/usr/bin/python3
"""Module 5-save_to_json_file.py.
writes an Object to a text file, using a JSON representation
"""


import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a JSON representation

    Args:
       - my_obj: object to write
       - filename: name of the file.
    """

    with open(filename, mode='w+') as myfile:
        json.dump(my_obj, myfile)
