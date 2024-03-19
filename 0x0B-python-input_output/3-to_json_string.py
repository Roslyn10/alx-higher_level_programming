#!/usr/bin/python3
"""Defines a function that returns JSON"""

import json


def to_json_string(my_obj):
    """A function that returns the JSON rep of an object"""

    return json.dumps(my_obj)
