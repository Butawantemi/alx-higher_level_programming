#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        self.size = size  # Using the setter to set the size

    @property
    def size(self):
        return self.__size  # Getter method to retrieve the size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value  # Setter method to set the size

    def area(self):
        return self.__size ** 2
