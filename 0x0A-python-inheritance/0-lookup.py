#!/usr/bin/python3
"""returns a list of available attributes and methods of an object"""
def lookup(obj):
    """return a list of strings, containing the names of attributes and methods of the obj"""
    return dir(obj)
