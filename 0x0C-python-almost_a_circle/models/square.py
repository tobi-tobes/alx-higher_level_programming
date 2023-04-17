#!/usr/bin/python3
"""
Square Class
This module contains the definition of the
Square Class, which inherits from Rectangle
"""


from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines the class Square that inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """initializes an instance of Square"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """retrieves the size attribute"""
        return super().width

    @size.setter
    def size(self, value):
        """sets the size attribute"""
        self.width = value
        self.height = value

    def __str__(self):
        """overrides the __str__ method"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        if args is not None and len(args) != 0:
            self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
                self.height = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.width = kwargs["size"]
                self.height = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """returns the dictionary representation of a Square"""
        dictionary = {}
        dictionary["id"] = self.id
        dictionary["size"] = self.width
        dictionary["x"] = self.x
        dictionary["y"] = self.y
        return dictionary
