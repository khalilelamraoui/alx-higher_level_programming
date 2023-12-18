#!/usr/bin/python3
import dis


def magic_calculation(a, b):
    output = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise ValueError("Too far")
            else:
                output += (a ** b) / i
        except ValueError:
            output = a + b
            break
    return output
