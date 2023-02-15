#!/usr/bin/python3
"""class Rectangle that defines a rectangle"""


class Rectangle:
    """initialization"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    """ width getter"""
    def width(self):
        return (self.__width)

    @width.setter
    """width setter"""
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    """ Height getter"""
    def height(self):
        return (self.__height)

    @height.setter
    """ Height setter"""
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
