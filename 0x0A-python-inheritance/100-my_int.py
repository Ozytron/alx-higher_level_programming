#!/usr/bin/python3
"""Myint class Module"""


class MyInt(int):
    """A MyInt class"""
    def __eq__(self, TheRest):
        """Overides and inverts == operator"""
        return int(self) != int(TheRest)

    def __ne__(self, TheRest):
        """Overides and inverts != operator"""
        return int(self) == int(TheRest)
