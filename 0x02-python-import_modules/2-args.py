#!/usr/bin/python
if __name__ == "__main__":
 import sys
 numArguments = len(sys.argv) - 1
 if numArguments == 0:
    print("0 arguments.")
 elif numArguments == 1:
    print("1 argument:")
 else:
    print("{} arguments:".format(numArguments))
 for i, arg in enumerate(sys.argv[1:], start=1):
    print("{}: {}".format(i, arg))
