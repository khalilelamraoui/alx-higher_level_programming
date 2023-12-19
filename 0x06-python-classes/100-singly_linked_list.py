#!/usr/bin/python3
"""Singly linked list module"""


class Node:
    """Node class"""
    def __init__(self, data, next_node=None):
        """Node class initialized"""
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """data getter"""
        return self.__data
    
    @data.setter
    def data(self, value):
        """data setter"""
        self.__data = value

    @property
    def next_node(self):
        """next_node getter"""
        return self.__next_node
    
    @next_node.setter
    def next_node(self, value):
        """next_node setter"""
        self.__next_node = value


class SinglyLinkedList:
    """Singly linked list class"""
    def __init__(self):
        """Singly linked list initialized"""
        self.__head = None

    def sorted_insert(self, value):
        """Inserting new_node in the correct sorted position in the list"""
        new_node = Node(value)
        if self.__head is None:
            self.__head = new_node
            return
        if self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
            return
        current = self.__head
        while current.next_node is not None:
            if current.next_node.data > value:
                break
            current = current.next_node
        new_node.next_node = current.next_node
        current.next_node = new_node

    def __str__(self):
        """returning the SinglyLinkedList instance"""
        result = []
        current = self.__head
        while current:
            result.append(str(current.data))
            current = current.next_node
        return '\n'.join(result)
