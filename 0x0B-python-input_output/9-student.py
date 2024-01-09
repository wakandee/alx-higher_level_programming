#!/usr/bin/python3
"""Module 9-student.py
Creates a student class
"""


class Student:
    """ a class Student that defines a student"""

    def __init__(self, first_name, last_name, age):
        """ a class Student that defines a student

        Args:
           - first_name: first name of student
           - last_name: last name of student
           - age: age of student
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dictionary representation of a
        Student instance (same as 8-class_to_json.py)
        """

        return self.__dict__
