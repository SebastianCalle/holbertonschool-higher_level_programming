#!/usr/bin/python3


class Node:
    """Node class"""

    def __init__(self, data, next_node=None):
        """Initializate atributtes"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Return the data"""
        return self.__data

    @data.setter
    def data(self, value):
        """Logic of correct values for data"""
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Return the next_node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Logic of correct next_node"""
        if value is not None and type(value) is not Node:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """class for a SinglyLinkedList"""
    def __init__(self):
        """Initializate atributtes"""
        self.__head = None

    def __str__(self):
        tmp = self.__head
        print_node = []
        while(tmp):
            print_node.sort()
            print_node.append(str(tmp.data))
            tmp = tmp.next_node

        print_node.sort(key=int)
        return ("\n".join(print_node))

    def sorted_insert(self, value):
        """Insert a node sorted"""

        if self.__head is None:
            new_nod = Node(value)
            new_nod.next_node = self.__head
            self.__head = new_nod
        else:
            new_nod = Node(value)
            new_nod.data = value
            new_nod.next_node = self.__head
            self.__head = new_nod
