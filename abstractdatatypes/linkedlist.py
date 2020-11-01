#!/usr/bin/python3
from structs import Decorators


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
        while temp.next is not None:
            print(temp)
            temp=temp.next
        print(temp)
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
    @Decorators.enforce_llassetnode_datatype
    def insert_first(self, node):
        """
        Warning! This method inserts at head position
        Overrides head
        """
        self._head = node
        self.increase_len
    
    @Decorators.enforce_llassetnode_datatype
    def insert_last(self, node):
        """
        Function to insert at the end of the linked list
        """
        if self.is_empty:
            self.insert_first(node)
            return
        start = self._head
        while start.next is not None:
            start=start.next
        start.next=node
        self.increase_len
    
    @Decorators.enforce_llassetnode_datatype
    def insert(self, node):
        self.insert_last(node)

    # Searching methods
    @Decorators.enforce_llassetnode_datatype
    def find(self, node):
        """
        Function to search the linked list
        param node: node item that needs to be search 
        return: True if node exists in list else False
        """
        temp=self._head

        if node==temp:
            return True
        
        # search until end of list
        while temp.next is not None:
            if temp.next==node:
                return True
            else:
                temp=temp.next
        # node does not exist
        return False
