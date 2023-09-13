#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_set = set()
    result = 0
    for item in my_list:
        if isinstance(item, int) and item not in unique_set:
            unique_set.add(item)
            result += item
    return result
