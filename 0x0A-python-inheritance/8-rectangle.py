#!/usr/bin/python3
"""A class representing a rectangle, inheriting from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometrys
class Rectangle(BaseGeometry):
    """Initializes a Rectangle instance with width and height"""
    def __init__(self, width, height):
        super().__init__()
        self.__width = width
        self.__height = height

        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)
