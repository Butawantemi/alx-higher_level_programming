#!/usr/bin/python3
"""define a class square"""        
class Square:
  
    """initilize new square with private instance attribute"""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")  
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
