#!/usr/bin/python3

from models.rectangle import Rectangle

r = Rectangle(10, 10, 10, 10, 10)

print(r)

r.update()

print(r)

r.update(89)

print(r)

r.update(89, 2)

print(r)

r.update(89, 2, 3)

print(r)

r.update(89, 2, 3, 4)

print(r)

r.update(89, 2, 3, 4, 5)

print(r)
