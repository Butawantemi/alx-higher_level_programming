#!/usr/bin/python3
"""Insert a line of text after each line containing a specific string in a file"""
def append_after(filename="", search_string="", new_string=""):
    """a function that inserts a line of text to a file"""
    with open(filename, "r") as f:
        text = f.readlines()

    with open(filename, "w") as fo:
        res = ""
        for line in text:
            res += line
            if search_string in line:
                res += new_string
        fo.write(res)
