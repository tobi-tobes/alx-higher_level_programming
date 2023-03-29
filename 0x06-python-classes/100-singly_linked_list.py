#!/usr/bin/python3
"""
Node Class

This module defines a class Node with given parameters
"""


class Node:
    """Defines a node of a singly-linked list"""
    def __init__(self, data, next_node=None):
        """Creates a new node with the given data and next_node parameters"""
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """Retrieves the value of the data attribute"""
        return (self.__data)

    @data.setter
    def data(self, value):
        """Updates the data attribute with the value given as an argument
        after checking that the value fits specific parameters"""
        if type(value) is not int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """Retrieves the value of the next_node attribute"""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """Updates the next_node attribute with the value given as an argument
        after checking that the value fits specific parameters"""
        if value is None or type(value) is Node:
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


"""
Node Class

This module defines a class Node with given parameters
"""


class SinglyLinkedList:
    """Defines a singly-linked list"""
    def __init__(self):
        """Creates a singly_linked list"""
        self.__head = None

    def sorted_insert(self, value):
        """inserts a new Node into the correct
sorted position in the list (increasing order)"""
        if self.__head is None or self.__head.data > value:
            self.__head = Node(value, self.__head)
        else:
            curr = self.__head
            while curr.next_node is not None and curr.next_node.data < value:
                curr = curr.next_node
            curr.next_node = Node(value, curr.next_node)

    def __str__(self):
        """allows list to be printable into stdout"""
        linked_list = ""
        temp = self.__head
        if temp is None:
            return (linked_list)
        while temp is not None:
            linked_list += str(temp.data)
            if temp.next_node is not None:
                linked_list += "\n"
            temp = temp.next_node
        return (linked_list)
