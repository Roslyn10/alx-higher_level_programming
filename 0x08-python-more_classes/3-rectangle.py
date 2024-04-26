#!/usr/bin/python3
"""A class Rectangle that defines a rectangle"""


class Rectangle:
    """Represents a rectangle"""

    def __init__(self, width=0, height=0):
        """
        Represents a rectangle shape

        width(int): the width of the rectangle
            
            Raises:
                TypeError: if width is not an int
                ValueError: if width is less than 0

        height(int): height of the rectangle

            Raises:
                TypeError: if height is not an int
                ValueError: if height is less than 0
        """
        
        self.width = width
        self.height = height

    @property
    def width(self):
        """The width of the rectangle"""
        return self.__width
        
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >=0")
        self.__width = value

    @property
    def height(self):
        """The height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the rectangle area"""
        return self.width * self.height

    def perimeter(self):
        """returns the perimeter of the rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)
