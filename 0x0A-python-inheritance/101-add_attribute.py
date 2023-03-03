#!/usr/bin/python3
"""Add new attribute module"""


def add_attribute(self, new_attribute, value):
    """adds a new attribute to an object if possible"""
    if hasattr(self, "__dict__") or \
        (hasattr(self, "__slots__") and name in self.__slots__):
        setattr(self, new_attribute, value)
    else:
        raise TypeError("can't add new attribute")
    
