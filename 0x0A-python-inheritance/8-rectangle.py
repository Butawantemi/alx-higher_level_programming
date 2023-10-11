#!/usr/bin/python3
"""A class representing a rectangle, inheriting from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry
class Rectangle(BaseGeometry):
    """Initializes a Rectangle instance with width and height"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
