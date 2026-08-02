#!/usr/bin/python3

from models.rectangle import Rectangle

if __name__ == "__main__":
    r1 = Rectangle(10, 2)
    print(r1.__dict__)

    r2 = Rectangle(2, 10)
    print(r2.__dict__)

    r3 = Rectangle(10, 2, 0, 0, 12)
    print(r3.__dict__)
