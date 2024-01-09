#!/usr/bin/python3
"""
Function that appends a string at the end of a text file
and returns the number of characters added
"""


def append_write(filename="", text=""):
    """Appends a string at the end of a text file
    and returns the number of characters added"""
    with open(filename, mode="a", encoding="utf-8") as f:
        f.write(text)
    return len(text)
