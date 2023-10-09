#!/usr/bin/python3
"""Add a new attribute to an object if it's possible, or raise a TypeError"""
def add_attribute(obj, name, value):
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
