#!/usr/bin/python3
"""Base class module"""
import json
import os


class Base:
    """Base class representing unique objects"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize an object with a unique id

        Args:
            id (int): The identifier for the object.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of list_dictionaries.

        Args:
            list_dictionaries (list): A list of dictionaries

        Returns:
            str: JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the Json string representation of list_objs to a file

        Arguments:
            list_objs (list): A list of instances inheriting from Base
        """
        if list_objs is None:
            list_objs = []

        class_name = cls.__name__
        filename = f"{class_name}.json"

        dict_list = [obj.to_dictionary() for obj in list_objs]
        json_string = cls.to_json_string(dict_list)

        with open(filename, 'w') as file:
            file.write(json_string)
