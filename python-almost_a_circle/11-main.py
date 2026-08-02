#!/usr/bin/python3

from models.square import Square

s1 = Square(5)
print(s1)
print(s1.size)
print(s1.area())

print("")

s1.size = 10
print(s1)
print(s1.size)
print(s1.area())
