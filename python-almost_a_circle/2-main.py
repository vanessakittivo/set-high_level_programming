#!/usr/bin/python3

from models.rectangle import Rectangle

r = Rectangle(10, 2)
print(r.width)
print(r.height)
print(r.x)
print(r.y)
print(r.id)

r.width = 20
r.height = 5
r.x = 1
r.y = 3

print(r.width)
print(r.height)
print(r.x)
print(r.y)
