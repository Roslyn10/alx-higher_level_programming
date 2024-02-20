#!/usr/bin/python3
"""Defines a function that checks both class and inheritance"""


def is_kind_of_class(obj, a_class):
    """ Checks if an object is an instance of, 
    or if the object is an instance of an inherited class

    Arguments:
        obj: An object that is a specific class
        a_class: The class to match the object to

    Returns:
        True: if the object matches the class and class inheritance
        False: if otherwise 

    """
    if isinstance(obj, a_class):
        return True
    return False 
