#!/usr/bin/python3
"""Deines a function that appends a string"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of text file and returns number of characters

    Arguments:
        filename (str): Name of the file to write in
        text (str): Text inserted into the file

    Returns:
    The number of characters appened

    """

    with open(filename, 'a', encoding='utf=8') as file:
        return file.write(text)
