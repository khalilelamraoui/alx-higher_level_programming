#!/usr/bin/python3
"""Singly linked list module"""


class Node:
    """Node class"""
    def __init__(self, data, next_node=None):
        """Node class initialized"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Data getter"""
        return self.__data

    @data.setter
    def data(self, value):
        """Data setter"""
        self.__data = value

    @property
    def next_node(self):
        """Next node getter"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Next node setter"""
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
        current = self.__head
        emptySTR = ""
        while current is not None:
            emptySTR += str(current.data) + "\n"
            current = current.next_node
        return emptySTR[:-1]
