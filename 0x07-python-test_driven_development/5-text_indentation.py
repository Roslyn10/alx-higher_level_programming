#!/usr/bin/python3
"""A function that prints a text with 2 lines
    after the '.', '?', ':' characters"""


def text_indentation(text):
    """
    Prints the text with 2 new lines after each '.', '?', and ':'
    Arguments:
        text (string): Input text

    Raises:
        TypeError: If text is not a string
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for char in text:
        if char in ['.', '?', ':']:
            print(char + '\n\n', end='')
        else:
            print(char, end='')
