#!/usr/bin/python3
def roman_to_int(roman_string):
    roman = type(roman_string)
    romanLength = len(roman_string)
    if roman_string is None or roman is not str:
        return 0
    roman_dictionary = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                        'C': 100, 'D': 500, 'M': 1000}
    roman_list = []
    for element in roman_string:
        roman_list.append(roman_dictionary[element])
    counter = 0
    for i in range(romanLength):
        if i + 1 == romanLength:
            counter += roman_list[i]
        elif roman_list[i] >= roman_list[i + 1]:
            counter += roman_list[i]
        else:
            counter -= roman_list[i]
    return counter
