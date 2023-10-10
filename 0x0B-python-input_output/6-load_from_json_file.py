#!/usr/bin/python3
"""from JSON"""
import json
"""load an object from a JSON"""
def load_from_json_file(filename):
    """Load an object from a JSON file and return it"""
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
