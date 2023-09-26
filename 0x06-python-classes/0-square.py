#!/usr/bin/python3
class Square:
    def __init__(self, side_length=0):
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2

    def perimeter(self):
        return 4 * self.side_length

    def __str__(self):
        return "<class '0-square.Square'> {}"
