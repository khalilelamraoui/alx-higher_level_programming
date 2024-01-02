#!/usr/bin/python3
"""
function that prints a square with the character #.
"""


def print_square(size):
    """
    print_square: prints a square with the character #.
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0 and type(size) is float:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
    if size == 0:
        print()


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")
