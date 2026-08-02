#!/usr/bin/python3

from models.rectangle import Rectangle

r = Rectangle(10, 10, 10, 10, 10)

print(r)

r.update(height=1)

print(r)

r.update(width=1, x=2)

print(r)

r.update(y=1, width=2, x=3, id=89)

print(r)

r.update(x=1, height=2, y=3, width=4)

print(r)
