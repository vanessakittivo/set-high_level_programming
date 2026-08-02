#!/usr/bin/python3

from models.square import Square

s1 = Square(5)
print(s1)
print(s1.area())

print("--")

s2 = Square(3, 1, 3)
print(s2)
print(s2.area())

print("--")

s3 = Square(7, 2, 1, 12)
print(s3)
print(s3.area())
