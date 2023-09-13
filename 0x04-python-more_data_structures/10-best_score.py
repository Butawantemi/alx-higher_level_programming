#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or a_dictionary == {}:
        return None
    best_key = max(a_dictionary, key=lambda j: a_dictionary[j])
    return best_key
