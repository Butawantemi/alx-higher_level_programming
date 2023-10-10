#!/usr/bin/python3
"""To object"""
import json
"""Parse JSON string to object"""
def from_json_string(my_str):
    """Parse a JSON string and return the corresponding Python data structure (object)"""
    return json.loads(my_str)
