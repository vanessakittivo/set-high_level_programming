#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    """Multiply all values using map."""
    return list(map(lambda x: x * number, my_list))
