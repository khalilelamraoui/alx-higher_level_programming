#!/usr/bin/python3
def uppercase(s):
    uppercase_string = ""
    for char in s:
        ascii_value = ord(char)
        if 97 <= ascii_value <= 122:
            upper_ascii_value = ascii_value - 32
            uppercase_string += "{}".format(chr(upper_ascii_value))
        else:
            uppercase_string += "{}".format(char)
    print(uppercase_string)
