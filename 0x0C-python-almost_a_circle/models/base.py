#!/usr/bin/python3
"""Module base.py
Defines a Base class of all other
classes in the project.
"""

import json
import os
import csv


class Base:
    """a class Base class with:
    private class attribute: __nb_objects
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialized class instance.

        Args:
           - id: id of the attribute
        """

        if type(id) != int and id is not None:
            raise TypeError("id must be an integer")
        if id is not None:
            self.id = id
        else:
             Base.__nb_objects += 1
             self.id = Base.__nb_objects

    @classmethod
    def to_json_string(list_dictionaries):
        """Returns the json string representation of list_dictionaries.

        Args:
           - list_dictionaries: list of dictionaries.
        Return: json string representation of list_dictionaries
        """

        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        if (type(list_dictionaries) != list or
            not all(type(x) == dict for x in list_dictionaries)):
            raise TypeError("list_dictionaries must be a list of dictionaries")

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the json string representation of list_objs to a file.

        Args:
           - list_objs: list of instances who inherits of Base.
        """
        """
        if type(list_objs) != list and list_objs is not None:
            raise TypeError("list_objs must be a list of instances")
        if any(issubclass(type(x), Base) is False for x in list_objs):
            raise TypeError("list_objs must be a list of instances")
        """

        if list_objs is None or list_objs == []:
            jstr = "[]"
        else:
            jstr = cls.to_json_string([o.to_dictionary() for o in list_objs])
        filename = cls.__name__ + ".json"
        with open(filename, mode='w+') as myfile:
            myfile.write(jstr)

    @classmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation.

        Args:
           - json_string: is a string representing a list of dictionaries.
        """

        l = []
        if json_string is not None or json_string != '':
            if type(json_string) != str:
                raise TypeError("json_string must be a string")
            l = json.loads(json_string)
        return l

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set.

        Args:
           - dictionary: used as **kwargs

        Return: instance created
        """
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances."""

        filename = cls.__name__ + ".json"
        l = []
        list_dicts = []
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                s = f.read()
                list_dicts = cls.from_json_string(s)
                for d in list_dicts:
                    l.append(cls.create(**d))
        return l

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes list_objs in CSV format, then save it to a file.

        Args:
           - list_objs: list of instances
        """

        if (type(list_objs) != list and
            list_objs is not None or
            not all(isinstance(x, cls) for x in list_objs)):
            raise TypeError("list_objs must be a list of instances")

        filename = cls.__name__ + ".csv"
        with open(filename, 'w') as f:
            if list_objs is not None:
                list_objs = [x.to_dictionary() for x in list_objs]
                if cls.__name__ == 'Rectangle':
                    fields = ['id', 'width', 'height', 'x', 'y']
                elif cls.__name__ == 'Square':
                    fields = ['id', 'size', 'x', 'y']
                writer = csv.DictWriter(f, fieldnames=fields)
                writer.writeheader()
                writer.writerows(list_objs)

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes CSV format from a file.

        Returns: list of instances
        """

        filenmae = cls.__name__ + ".csv"
        l = []
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                reader = csv.reader(f, delimeter=',')
                if cls.__name__ == 'Rectangle':
                    fields = ['id', 'width', 'height', 'x', 'y']
                elif cls.__name__ == 'Square':
                    fields = ['id', 'size', 'x', 'y']
                for x, row in enumerate(reader):
                    if x > 0:
                        i = cls(1, 1)
                        for j, e in enumerate(row):
                            if e:
                                setattr(i, fields[j], int(e))
                        l.append(i)
        return l

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Opens a window and draws all the Rectangles and Squares.

        Args:
           - list_rectangles: list of all rectangles
           - list_squares: list of all squares
        """

        import turtle
        import time
        from random import randrange

        t = turtle.Turtle()
        turtle.bgcolor("white")
        t.color("black", "cyan")
        t.pensize(5)
        t.shape("square")

        for i in (list_rectangles + list_squares):
            t.penup()
            t.setpos(0, 0)
            turtle.Screen().colormode(255)
            t.pencolor((randrange(255), randrange(255), randrange(255)))
            Base.draw_rect(t, i)
            time.sleep(1)
        time.sleep(5)

    @staticmethod
    def draw_rect(t, rect):
        """Method to draw a rectangle or square."""

        t.penup()
        t.setpos(rect.x, rect.y)
        t.pendown()
        t.forward(rect.width)
        t.left(90)
        t.forward(rect.height)
        t.left(90)
        t.forward(rect.width)
        t.left(90)
        t.forward(rect.height)
