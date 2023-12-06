#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    multiply_func = lambda x: x * number
    result = map(multiply_func, my_list)
    return list(result)
