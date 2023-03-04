#!/usr/bin/python3
"""File-writing function."""


def write_file(filename="", text=""):
    """Write a string to a UTF8 text file.
    Function Arguments:
        filename (str): The name of the file to write.
        text (str): The text to write to the file.
    Function Returns:
        The number of characters written to file.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
