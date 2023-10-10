#!/usr/bin/python3
"""a class representing a student"""
class Student:
    """initializes a Student instance with first_name, last_name, and age """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    """retrieve a dictionary representation of a Student instance"""
    def to_json(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age
        }
