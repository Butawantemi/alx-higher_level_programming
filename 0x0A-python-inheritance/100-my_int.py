#!/usr/bin/python3
"""Write a class MyInt that inherits from int"""
class MyInt(int):
    """A subclass of class int"""
    def __eq__(self, other):
        """sets the behaviour of == """
        return super().__ne__(other)
    """sets the != behavior"""
    def __ne__(self, other):
        return super().__eq__(other)
