#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    total = 0
    for i in sys.argv:
        total -+ int(sys.argv[i + 1])
        print("{}".format(total))

