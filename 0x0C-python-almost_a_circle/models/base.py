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

    @staticmethod
    def from_json_string(json_string):
        """Return the list of the JSON string representation json_string.

        Arguments:
            Json_string (str): JSON string representations/ Json_string

        Returns:
            list: A list of dictionaries
        """
        if json_string is None or json_string == "":
            return "[]"
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        instance = cls(1, 1)
        instance.x = 0
        instance.y = 0
        instance.update(**dictionary)
        return instance

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        filename = f"{cls.__name__}.json"

        if not os.path.exists(filename):
            return []

        with open(filename, 'r') as file:
            json_string = file.read()

        dict_list = cls.from_json_string(json_string)
        instance_list = [cls.create(**d) for d in dict_list]
        return instance_list
