#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
numberAbs = abs(number)
lastDigit = numberAbs % 10
sign = ''
if number < 0 and lastDigit > 0:
    sign = '-'
elif number < 0 and lastDigit == 0:
    sign = ''
print(f"Last digit of {number} is {sign}{lastDigit} and is", end=" ")

if number < 0 and lastDigit > 0:
    print("less than 6 and not 0")
# elif number < 0 and lastDigit == 0:
#     print("0")
else:
    if lastDigit > 5:
        print("greater than 5")
    elif lastDigit == 0:
        print("0")
    else:
        print("less than 6 and not 0")
