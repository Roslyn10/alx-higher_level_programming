#!/usr/bin/python3
"""Base class module"""
import json
import os
import csv


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
        """Write the JSON string representation of list_objs to a file

        Args:
            list_objs (list): A list of instances inheriting from Base
        """
        if list_objs is None:
            list_objs = []

        filename = f"{cls.__name__}.json"
        dict_list = [obj.to_dictionary() for obj in list_objs]
        json_string = cls.to_json_string(dict_list)

        with open(filename, 'w') as file:
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """Return the list of the JSON string representation json_string.

        Args:
            json_string (str): JSON string representations

        Returns:
            list: A list of dictionaries
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes a list of objects to a CSV file."""
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Returns a list of instances from a CSV file."""
        filename = f"{cls.__name__}.csv"

        if not os.path.exists(filename):
            return []

        with open(filename, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            dict_list = [
                    dict((k, int(v)) for k, v in d.items()) for d in reader
                    ]
        instance_list = [cls.create(**d) for d in dict_list]
        return instance_list
