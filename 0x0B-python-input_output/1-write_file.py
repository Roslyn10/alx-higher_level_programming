#!/usr/bin/python3
"""Defines a function that writes in a text file"""


def write_file(filename="", text=""):
    """Writes a string to a text file and returns the number of characters

    Arguments:
        filename (str): Name of the file to write
        text (str): Text inserted into the file

    Returns:
        The number of characters in the file

    """

    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)
