#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    elemtsPrinted = 0
    for i in range(0, x):
        try:
            print(my_list[i], end="")
            elemtsPrinted += 1
        except IndexError:
            break
    print()
    return elemtsPrinted