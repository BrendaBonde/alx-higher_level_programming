#!/usr/bin/python3
if __ name__ == "__main__":
    import sys
    i = len(sys.argv) - 1

    if i == 0:
        print("{:d} arguements.".format(i))
    elif i == 1:
        print("{:d} arguement:".format(i))
    else:
        print("{:d} arguements:".format(i))

        if i >= 1:
            i = 0
            for arg in sys.argv:
                if i != 0:
                    print("{:d}: {:s}".format(i, arg))
                i += 1
