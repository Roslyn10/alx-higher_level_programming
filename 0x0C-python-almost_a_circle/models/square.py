#!/usr/bin/python3
"""A Square class that inherits from rectangle"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes a Square instance"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """String representation of a square"""
        return (
            f"[Square] ({self.id}){self.x}/{self.y} - "
            f"{self.width}"
        )

    @property
    def size(self):
        """Width getter"""
        return self.width

    @size.setter
    def size(self, value):
        """Size setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be >= 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute"""
        if args and len(args) != 0:
        for i in range(len(args)):
            if i == 0:
                if args[i] is None:
                    self.__init__(self.width, self.width, self.x, self.y)
                else:
                    self.id = args[i]
            if i == 1:
                self.width = args[i]
                self.height = args[i]
            if i == 2:
                self.x = args[i]
            if i == 3:
                self.y = args[i]
    else:
        if kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.width, self.width, self.x, self.y)
                    else:
                        self.id = value
                elif key == "size":
                    self.width = value
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """Returns the dictionary representation of a square"""

        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
