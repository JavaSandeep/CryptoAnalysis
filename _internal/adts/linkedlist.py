#!/usr/bin/python3
from structs import Decorators


from structs import LinkedListNode


class LinkedList:
    """
    Linked list implementation in python
    Uses structs.AssetNode as node items
    """

    length=0

    def __init__(self):
        self._head = None


    def __str__(self):
        temp=self._head
        print(temp)
        while temp.next is not None:
            print(temp.next)
            temp=temp.next
        return "End of list"

    @property
    def is_empty(self):
        if self._head is None:
            return True
        return False

    @property
    def increase_len(self):
        self.length+=1

    # Insert methods
    def insert_first(self, node):
        """
        Warning! This method inserts at head position
        Overrides head
        """
        node=LinkedListNode(node)
        self._head = node
        self.increase_len
    
    def insert_last(self, node):
        """
        Function to insert at the end of the linked list
        """
        if self.is_empty:
            self.insert_first(node)
            return

        # It is important that node typecast is done below here
        node=LinkedListNode(node)
        start = self._head
        while start.next is not None:
            start=start.next
        start.next=node
        self.increase_len
    
    def insert(self, node):
        self.insert_last(node)

    # Searching methods
    def find(self, node):
        """
        Function to search the linked list
        param node: node item that needs to be search 
        return: True if node exists in list else False
        """
        if self.is_empty:
            print("Warning. List is empty")
            return False
    
        temp=self._head

        if node==temp.data_obj:
            return True
        
        # search until end of list
        while temp.next is not None:
            if temp.next.data_obj==node:
                return True
            else:
                temp=temp.next
        # node does not exist
        return False
