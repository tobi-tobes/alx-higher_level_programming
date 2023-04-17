#!/usr/bin/python3
"""
Rectangle Class
This module contains the definition of the
Rectangle Class, which is inherits from Base
"""


from models.base import Base


class Rectangle(Base):
    """Defines the class Rectangle that inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Creates an instance of a Rectangle"""
        self.dimension_validator("width", width)
        self.dimension_validator("height", height)
        self.position_validator("x", x)
        self.position_validator("y", y)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    def dimension_validator(self, attr, value):
        """validates the height and width input"""
        if type(value) is not int:
            raise TypeError(f"{attr} must be an integer")
        elif value <= 0:
            raise ValueError(f"{attr} must be > 0")

    def position_validator(self, attr, value):
        """validates the x and y input"""
        if type(value) is not int:
            raise TypeError(f"{attr} must be an integer")
        elif value < 0:
            raise ValueError(f"{attr} must be >= 0")

    @property
    def width(self):
        """retrieves the width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the width attribute"""
        self.dimension_validator("width", value)
        self.__width = value

    @property
    def height(self):
        """retrieves the height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the height attribute"""
        self.dimension_validator("height", value)
        self.__height = value

    @property
    def x(self):
        """retrieves the x attribute"""
        return self.__x

    @x.setter
    def x(self, value):
        """sets the x attribute"""
        self.position_validator("x", value)
        self.__x = value

    @property
    def y(self):
        """retrieves the y attribute"""
        return self.__y

    @y.setter
    def y(self, value):
        """sets the y attribute"""
        self.position_validator("y", value)
        self.__y = value

    def area(self):
        """computes the area of a Rectangle"""
        return self.__width * self.__height

    def display(self):
        """prints in stdout the Rectangle instance with the character #"""
        width = self.__width
        height = self.__height
        x = self.__x
        y = self.__y
        for m in range(y):
            print()
        for i in range(height):
            for j in range(x):
                print(" ", end="")
            for k in range(width):
                print("#", end="")
            if i != height - 1:
                print()
        print()

    def __str__(self):
        """overrides the __str__ method"""
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} -\
 {self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        if args is not None and len(args) != 0:
            self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        dictionary = {}
        dictionary["id"] = self.id
        dictionary["width"] = self.width
        dictionary["height"] = self.height
        dictionary["x"] = self.x
        dictionary["y"] = self.y
        return dictionary
