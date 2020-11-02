#!/usr/bin/python3

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
        if idx > (self.length-1):
            print("Error. Index out of order")
            return False
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

    # sorting mechanism
    # uses selection sort
    def sort(self, key):
        """
        Function to perform sorting based on attribute (Selection sort is used)
        params key: key using which sorting needs to be performed
        """
        for j in range(self.length):
            min_idx=j
            for k in range(j+1, self.length):
                if self.get_index(min_idx).get_attribute(key) > self.get_index(k).get_attribute(key):
                    min_idx=k
            
            # Swap the found minimum to the initial position
            tmp_obj = self.get_index(j)
            self.set_index(j, self.get_index(min_idx))
            self.set_index(min_idx, tmp_obj)
        return self