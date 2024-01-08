#!/usr/bin/python3
"""
Module that contains a class MyList
"""


class MyList(list):
    """
    MyList class that inherits from list
    """
    def print_sorted(self):
        """
        prints the list in ascending sort
        """
        print(sorted(self))
