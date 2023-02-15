#!/usr/bin/python3
"""class Rectangle that defines a rectangle"""


class Rectangle:
    """
    Defines a rectangle by:
    private instance attribute: width (int)
    private instance attribute: height (int)
    initializes width and height
    """

    def __init__(self, width=0, height=0):
        """initialization"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """ width getter"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """width setter"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Height getter"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """ Height setter"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
