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
