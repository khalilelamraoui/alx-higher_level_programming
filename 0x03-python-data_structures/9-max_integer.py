#!/usr/bin/python3


def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    else:
        max = my_list[0]
        for i in range(0, len(my_list) - 1):
            if max <= my_list[i + 1]:
                max = my_list[i + 1]
        return max
