#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) != str or roman_string is None:
        return 0
    roman_dictionary = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                        'C': 100, 'D': 500, 'M': 1000}
    roman_list = []
    for element in roman_string:
        roman_list.append(roman_dictionary[element])
    counter = 0
    for i in range(len(roman_string)):
        if i + 1 == len(roman_string):
            counter += roman_list[i]
        elif roman_list[i] >= roman_list[i + 1]:
            counter += roman_list[i]
        else:
            counter -= roman_list[i]
    return counter
