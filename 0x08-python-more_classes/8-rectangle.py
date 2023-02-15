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
    repr() return a string representation of the rectangle to be
    able to recreate a new instance by using eval()
    Print the message Bye rectangle... when an instance of Rectangle
    is deleted.
    number_of_instances: keep track of the number of instances remaining.
    print_symbol: holds the symbol of any type to use and print rectangle.
    Static method def bigger_or_equal(rect_1, rect_2): that returns the
    biggest rectangle based on the area.
    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """initialization"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        """rectangle as print_symbol"""
        if self.width == 0 or self.height == 0:
            return ''
        what_to_print = ''
        for row in range(self.height):
            for col in range(self.width):
                what_to_print += str(self.print_symbol)
            if row != self.height - 1:
                what_to_print += '\n'
        return (what_to_print)

    def __repr__(self):
        """return a string representation of the rectangle and
           able to recreate a new instance by using eval()
        """
        return "Rectangle(" + str(self.width) + ", " + str(self.height) + ")"

    def __del__(self):
        """delete instance"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ get the rectangle with bigger area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
