#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5

    addition = add(a, b)
    subtraction = sub(a, b)
    multiplication = mul(a, b)
    division = div(a, b)

    print("{:d} + {:d} = {:d}".format(a, b, addition))
    print("{:d} - {:d} = {:d}".format(a, b, subtraction))
    print("{:d} * {:d} = {:d}".format(a, b, multiplication))
    print("{:d} / {:d} = {:d}".format(a, b, division))
