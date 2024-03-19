#!/usr/bin/python3
"""Defines an Object writing function"""

import json


def save_to_json_file(my_obj, filename):
    """A function that writes an object to text file, using JSON"""

    with open(filename, 'w') as file:
        json.dump(my_obj, file)
