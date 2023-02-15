#!/usr/bin/python3
"""class Rectangle that defines a rectangle"""


class Rectangle:
    """
    Defines a rectangle by:
    private instance attribute: width (int)
    private instance attribute: height (int)
    initializes width and height
    Public instance method: def area(self)
    Public instance method: def perimeter(self)
    print() and str() should print the rectangle with the character #
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

    def area(self):
        """Area of rectangle"""
        return (self.width * self.height)

    def perimeter(self):
        """Perimeter of rectangle"""
        if self.width == 0 or self.height == 0:
            return (0)
        return ((self.width * 2) + (self.height * 2))
    def __str__(self):
        """rectangle as #"""
        if self.width == 0 or self.height == 0:
            return ''
        what_to_print = ''
        for row in range(self.height):
            for col in range(self.width):
                what_to_print += '#'
            if row != self.height - 1:
                what_to_print += '\n'
        return (what_to_print)
