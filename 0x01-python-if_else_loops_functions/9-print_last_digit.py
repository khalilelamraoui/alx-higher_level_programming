#!/usr/bin/python3

def print_last_digit(number):
    absoluteNum = abs(number)
    last_digit = absoluteNum % 10
    print(last_digit, end='')
    return last_digit
