#!/usr/bin/python3
"""A function that prints names"""


def say_my_name(first_name, last_name=""):
    """ Prints Names

    Arguments:
    first_name(str): The first name to be printed
    last_name(str): The last name to be printed

    Raises:
        TypeError: If first_name is not string
        TypeError: If last_name is not string

    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
