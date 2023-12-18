#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    elemtsPrinted = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            elemtsPrinted += 1
        except ValueError:
            continue
        except TypeError:
            continue
    print()
    return elemtsPrinted
