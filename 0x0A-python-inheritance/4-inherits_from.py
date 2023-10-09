#!/usr/bin/python3
"""check if obj is an instance of a class that inherits from a_class"""
def inherits_from(obj, a_class):
    """
    check if obj is an instance of a class that inherits from a_class.
    returns True if it is, False otherwise.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
