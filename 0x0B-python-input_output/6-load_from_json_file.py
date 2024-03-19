#!/usr/bin/python3
"""Defines an object creating function from JSON file"""


import json


def load_from_json_file(filename):
    """A function that creates an Object from a "JSON file" """

    with open(filename, 'r') as file:
        return json.load(file)
