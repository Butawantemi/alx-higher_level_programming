#!/usr/bin/python3

"""The module"""
class MyList(list):
    """A subclass of list"""
    def __init__(self):
        """Initialize the object"""
        super().__init__()

    def print_sorted(self):
        """Prints the sorted list"""
        print(sorted(self))
