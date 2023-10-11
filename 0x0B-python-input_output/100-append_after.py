#!/usr/bin/python3
"""Insert a line of text after each line containing a specific string in a file"""
def append_after(filename="", search_string="", new_string=""):
    res = []
    
    with open(filename, 'r') as file:
        for line in file:
            res.append(line)
            if search_string in line:
                res.append(new_string)
    
    with open(filename, 'w') as file:
        file.writelines(res)
