#!/usr/bin/python3
"""Square class Module"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Square class"""
    def __init__(self, size):
        """instantiation"""
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """returns area of Square"""
        return self.__size ** 2

    def __str__(self):
        """returns a string"""
        return "[Square] {}/{}".format(self.__size, self.__size)
