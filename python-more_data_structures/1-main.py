#!/usr/bin/python3

search_replace = __import__('1-search_replace').search_replace

my_list = [1, 2, 3, 4, 3]

new_list = search_replace(my_list, 3, 9)

print(my_list)
print(new_list)
