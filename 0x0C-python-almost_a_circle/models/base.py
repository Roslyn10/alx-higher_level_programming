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
