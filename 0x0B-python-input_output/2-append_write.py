#!/usr/bin/python3
"""File-appending function."""


def append_write(filename="", text=""):
    """Appends a string to the end of a UTF8 text file.
    Function Arguments:
        filename (str): The name of the file to append to.
        text (str): The string to append to the file.
    Function Returns:
        The number of characters appended on file.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
