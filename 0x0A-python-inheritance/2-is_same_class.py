#!/usr/bin/python3
"""the module is 2-is_same_class"""
def is_same_class(obj, a_class):
    """
    Check if obj is an instance of a_class.
    Returns True if they match, False otherwise.
    """
    return type(obj) is a_class
