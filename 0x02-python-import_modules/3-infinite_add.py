#!/usr/bin/python
if __name__ == "__main__":
 import sys
 if len(sys.argv) < 2:
    print("0")
 else:
    res = 0
    for arg in sys.argv[1:]:
        res += int(arg)
    print("{}".format(res))

