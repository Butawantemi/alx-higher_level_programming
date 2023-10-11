#!/usr/bin/python3
"""Generate Pascal's triangle up to the nth row"""
def pascal_triangle(n):
    """returns a list of lists of integers representing the Pascal’s triangle"""
    triangle = []
    if n <= 0:
        return triangle
    if n == 0:
        return [[1]]

    triangle = [[1]]
    for i in range(n-1):
        triangle.append([a+b for a, b in zip([0] + triangle[-1], triangle[-1] + [0])])
    return triangle
