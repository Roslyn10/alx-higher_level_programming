#!/usr/bin/python3
"""A class Rectangle that defines a rectangle"""


class Rectangle:
    """Represents a triangle"""

    def __init__(self, width=0, height=0):

        """
        Represents retangle shape

    
        width (int): width of the rectangle

            Raises: 
            TypeError: if width not an int
            ValueError: If width is less than 0

        height (int): height of the rectangle

            Raises:
            TypeError: if height is not an int
            ValueError: if height is less than 0
        """
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("Width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
