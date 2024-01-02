#!/usr/bin/python3
"""
function that prints My name is <first name> <last name>
"""


def say_my_name(first_name, last_name=""):
    """
    say_my_name: prints My name is <first name> <last name>
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    if first_name is None:
        raise TypeError("first_name must be a string")
    if last_name is None:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/3-say_my_name.txt")
