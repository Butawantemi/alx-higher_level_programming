#!/usr/bin/python3
for j in range(ord('a'), ord('z')+1):
    if chr(j) not in ['q', 'e']:
        print("{}".format(chr(j)), end="")
