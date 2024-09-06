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
            f"[Square] ({self.id}) {self.x}/{self.y} - "
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
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute"""
        if args:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]

        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of a square"""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
