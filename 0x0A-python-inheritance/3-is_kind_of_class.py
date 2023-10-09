#!/usr/bin/python3
def is_kind_of_class(obj, a_class):
    """
    check if obj is an instance of, or inherited from, a_class.
    returns True if it is, False otherwise.
    """
    return isinstance(obj, a_class)

