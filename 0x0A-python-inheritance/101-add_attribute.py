#!/usr/bin/python3
"""Add new attribute module"""


def add_attribute(obj, new_attribute, value):
    """adds a new attribute to an object if possible"""
    if hasattr(obj, "__dict__") or \
       (hasattr(obj, "__slots__") and new_attribute in obj.__slots__):
        setattr(obj, new_attribute, value)
    else:
        raise TypeError("can't add new attribute")
