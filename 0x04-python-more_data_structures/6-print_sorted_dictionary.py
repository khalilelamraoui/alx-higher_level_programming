#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sortedDict = sorted(a_dictionary)
    for element in sortedDict:
        print("{}: {}".format(element, a_dictionary[element]))
