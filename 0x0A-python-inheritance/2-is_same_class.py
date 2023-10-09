#!/usr/bin/python3
"""checks if an object is exactly an instance of the specified class"""
def is_same_class(obj, a_class):
    """
    Check if obj is an instance of a_class.
    Returns True if they match, False otherwise.
    """
    return type(obj) is a_class
