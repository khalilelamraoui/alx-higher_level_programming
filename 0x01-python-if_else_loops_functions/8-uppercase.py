#!/usr/bin/python3
def uppercase(s):
    for char in s:
        ascii_value = ord(char)
        if 97 <= ascii_value <= 122:
            upper_ascii_value = ascii_value - 32
            print("{}".format(chr(upper_ascii_value)), end='')
        else:
            print("{}".format(char), end='')
    print()
