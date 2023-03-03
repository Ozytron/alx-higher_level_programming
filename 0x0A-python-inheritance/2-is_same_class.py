#!/usr/bin/python3
"""is the same module"""


def is_same_class(obj, a_class):
    """function returns True if the object is exactly an instance
       of the specified class.
       otherwise: return False."""
    return type(obj) == a_class
