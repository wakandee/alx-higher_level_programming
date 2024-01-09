#!/usr/bin/python3
"""Module 10-student.py
Creates a student class
(based on 9-student.py)
"""


class Student:
    """ a class Student that defines a student"""

    def __init__(self, first_name, last_name, age):
        """ a class Student that defines a student
         (based on 9-student.py)
        Args:
           - first_name: first name of student
           - last_name: last name of student
           - age: age of student
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a
        Student instance (same as 8-class_to_json.py)

        Args:
           - attrs: list of attributes

        Return: the dict representation of the instance.
        """

        my_dict = dict()
        if type(attrs) is list and all(type(x) is str for x in attrs):
            for x in attrs:
                if x in self.__dict__:
                    my_dict.update({x: self.__dict__[x]})
            return my_dict
        return self.__dict__.copy()
