#!/usr/bin/python3
def uppercase(str):
    for c in "{}".format(str):
        if ord(c) >= ord('a') and ord(c) <= ord('z'):
            c = chr(ord(c) - 32)
        print("{}".format(c), end="")
    print()
