#!/usr/bin/python3
class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and type(value) is not Node:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        new = Node(value)

        if self.__head is None or value < self.__head.data:
            new.next_node = self.__head
            self.__head = new
            return

        current = self.__head

        while current.next_node and current.next_node.data < value:
            current = current.next_node

        new.next_node = current.next_node
        current.next_node = new

    def __str__(self):
        values = []
        current = self.__head

        while current:
            values.append(str(current.data))
            current = current.next_node

        return "\n".join(values)
