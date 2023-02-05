#!/usr/bin/python3
"""
This function returns the integer addition of a and b.
If a or b is float, it is typcasted to integer before suming.
TypeError is raised if a or b is not integer or not float.
"""
def add_integer(a, b=98):
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
