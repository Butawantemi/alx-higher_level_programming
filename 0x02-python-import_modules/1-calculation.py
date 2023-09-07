#!/usr/bin/python3
if __name__ == "__main__":
 from calculator_1 import add, sub, mul, div
 a = 10
 b = 5
 Addition = add(a, b)
 Substraction = sub(a, b)
 Multiplicatin = mul(a, b)
 Division = div(a,b)
 print("{} + {} = {}".format(a, b, Addition))
 print("{} - {} = {}".format(a, b, Substraction))
 print("{} * {} = {}".format(a, b, Multiplicatin))
 print("{} / {} = {}".format(a, b, Division))
