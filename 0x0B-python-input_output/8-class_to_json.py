#!/usr/bin/python3
"""Defines a function that returns the dictionary description"""


import json


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure for JSON
    (list, dictionary, string, integer and boolean
    """

    return obj.__dict__
