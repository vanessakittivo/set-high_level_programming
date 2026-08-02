#!/usr/bin/python3

from models.rectangle import Rectangle

r1 = Rectangle(10, 2, 1, 9)

d = r1.to_dictionary()

print(type(d))
print(d)

r2 = Rectangle(1, 1)

print(r2)

r2.update(**d)

print(r2)

print(r1 == r2)
