#!/usr/bin/python3
from __future__ import absolute_import

from .structs import LinkedListNode


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
        outputt=str(temp.data_obj.__str__())
        while temp.next is not None:
            outputt+=str(temp.next.data_obj.__str__())
            temp=temp.next
        return outputt

    @property
    def is_empty(self):
        if self._head is None:
            return True
        return False

    @property
    def _increase_len(self):
        self.length+=1

    def _relloc(self, prev, node):
        if prev is None:
            # The node is head # Head also has two condition
            # Single item list or multi item list
            if self.length==1:
                self._head=None
            else:
                self._head=node.next
        else:
            prev.next=node.next
        return

    def print_same_line(self):
        if self.length==0:
            return "Empty"
        temp=self._head
        outputt=temp.data_obj.get_symbol
        while temp.next is not None:
            outputt+=(' -> '+temp.next.data_obj.get_symbol)
            temp=temp.next
        return outputt

    # Insert methods
    def insert_first(self, node):
        """
        Warning! This method inserts at head position
        Overrides head
        """
        node=LinkedListNode(node)
        self._head = node
        self._increase_len
    
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
        self._increase_len
    
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

    def get_item(self, pk):
        """
        In this case pk is symbol
        """
        if self.is_empty:
            print("Warning. List is empty")
            return None
    
        temp=self._head

        if temp.data_obj.get_symbol==pk:
            return temp.data_obj
        
        # search until end of list
        while temp.next is not None:
            if temp.next.data_obj.get_symbol==pk:
                return temp.next.data_obj
            else:
                temp=temp.next
        # node does not exist
        return None

    # indexing methods
    def get_index(self, idx):
        """
        Getting the indexed element, index begins at 0
        """
        if idx > (self.length-1):
            print("Error. Index out of order")
            return None
        if self.is_empty:
            print("Warning. List is empty")
            return None

        temp=self._head

        if idx==0:
            return temp.data_obj

        # search until end of list
        idx_counter=1
        while temp.next is not None:
            if idx==idx_counter:
                return temp.next.data_obj
            else:
                idx_counter+=1
                temp=temp.next

    def set_index(self, idx, data_obj):
        if 0 <= idx <= (self.length-1):
            if self.is_empty:
                print("Warning. List is empty")
                return False
            
            if idx==0:
                self._head.data_obj=data_obj
                return True
            
            temp=self._head

            # search until end of list
            # The counter is indexing to the next element
            idx_counter=1
            while temp.next is not None:
                if idx==idx_counter:
                    temp.next.data_obj=data_obj
                    return True
                else:
                    idx_counter+=1
                    temp=temp.next
        else:
            print("Error. Index out of order")
            return False

    def remove(self, node):
        if self.is_empty:
            print("Warning. List is empty")
            return False
        # Head, last node, any middle node
        prev=None
        temp=self._head

        # Head condition
        if temp.data_obj==node:
            self._relloc(None, temp)
            self.length-=1
            return True

        # search until end of list
        while temp.next is not None:
            if temp.data_obj==node:
                self._relloc(prev, temp)
                self.length-=1
                return True
            else:
                prev=temp
                temp=temp.next
        # node does not exist

        # Tail condition
        if temp.data_obj==node:
            self._relloc(prev, temp)
            self.length-=1
            return True
        ##########
        print("Node not found")
        return False

    def remove_head(self):
        return self.remove(self._head.data_obj)
    
    def remove_last(self):
        """
        Function that removes the last element, similar to pop
        """
        if self.is_empty:
            print("Warning. List is empty")
            return False
        temp=self._head
        # search until end of list
        while temp.next is not None:
            temp=temp.next
        
        return self.remove(temp.data_obj)

    # sorting mechanism
    # uses selection sort
    def sort(self, key, inverse=False):
        """
        Function to perform sorting based on attribute (Selection sort is used)
        params key: key using which sorting needs to be performed
        """
        for j in range(self.length):
            min_idx=j
            for k in range(j+1, self.length):
                if not inverse:
                    if self.get_index(min_idx).get_attribute(key) > self.get_index(k).get_attribute(key):
                        min_idx=k
                else:
                    if self.get_index(min_idx).get_attribute(key) < self.get_index(k).get_attribute(key):
                        min_idx=k
            
            # Swap the found minimum to the initial position
            tmp_obj = self.get_index(j)
            self.set_index(j, self.get_index(min_idx))
            self.set_index(min_idx, tmp_obj)
        return self