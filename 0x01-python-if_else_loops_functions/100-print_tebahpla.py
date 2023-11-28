#!/usr/bin/python3

for c in range(ord('z'), ord('a') - 1, -2):
    print("{0}{1}".format(chr(c), chr(c - 33)), end="")
