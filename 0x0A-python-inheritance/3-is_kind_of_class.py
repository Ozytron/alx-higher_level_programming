#!/usr/bin/python3
"""same class or inherit from - module"""


def is_kind_of_class(obj, a_class):
    """function returns True if the object is an instance of,
       or if the object is an instance of a class that inherited from,
       the specified class. 
       otherwise: return False."""
    return isinstance(obj, a_class)
