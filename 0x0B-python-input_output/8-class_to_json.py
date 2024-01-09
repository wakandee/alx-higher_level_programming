#!/usr/bin/python3
"""Module 8-class_to_json.py
returns the dictionary description with simple data structure
(list, dictionary, string, integer and boolean)
for JSON serialization of an object:
"""


def class_to_json(obj):
    """Creates a dict description of obj.

    Args:
       - obj: object to serialize.
    Return: dictioanary description of an obj
    """

    return obj.__dict__
