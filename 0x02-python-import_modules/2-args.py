#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argc = len(sys.argv)
    if argc == 1:
        print("{} arguments.".format(argc - 1))
    elif argc == 2:
        print("{} argument:".format(argc - 1))
        print("1: {:s}".format(sys.argv[1]))
    else:
        print("{:d} arguments:".format(argc - 1))
        for i in range(1, argc):
            print("{:d}: {:s}".format(i, sys.argv[i]))
