#!/usr/bin/python3

######################
# The Graph will be implemented using Adjanceny list 
from __future__ import absolute_import

from copy import deepcopy
import traceback

from .linkedlist import LinkedList


class Graph:
    """
    Class implemention for the graph
    """
    def __init__(self):
        # List of Asset nodes
        self.vertices=LinkedList()

        # List of the trade edges
        self.edges=LinkedList()

        # List of paths
        self.list_paths=LinkedList()
    
    def __str__(self):
        return self.edges.__str__()

    def add_vertex(self, node):
        """
        Function to add vertex, adding vertex would be private
        """
        if not self.vertices.find(node):
            self.vertices.insert(
                node)

    def _is_adjacent(self, curr_node, end_node):
        """
        Function to find adjacent nodes, it's private method
        """
        # Edge case for detecting same nodes
        if curr_node==end_node:
            return False

        # Check if there is any edge made by curr node and end node
        temp_node=self.edges._head
        # temp node is the item in edges list, Thus it must be accessed as follows
        # temp_node -> data_obj -> start_node -> data_obj
        while temp_node.next is not None:
            if ((temp_node.data_obj.start_node==curr_node) and\
                 (temp_node.data_obj.end_node==end_node)):
                return True
            temp_node=temp_node.next
        # check for the last not
        return ((temp_node.data_obj.start_node==curr_node) and\
            (temp_node.data_obj.end_node==end_node))

    def reset_list_path(self):
        self.list_paths=LinkedList()

    def add_edge(self, edge):
        """
        Function to add edges to the graph
        returns: True if success else False
        """
        try:
            self.add_vertex(edge.start_node)
            self.add_vertex(edge.end_node)
            # adding to edges
            self.edges.insert(
                edge
            )
            return True
        except Exception as ex:
            print("ERROR: Add edge function failed {0}".format(ex))
            traceback.print_exc()
            return False

    def get_edge_count(self):
        return self.edges.length

    def get_vertex_count(self):
        return self.vertices.length

    def get_adjacent(self, curr_node):
        """
        Function to get all adjacent nodes to given node
        """
        adjacentNodesList = LinkedList()

        temp_node=self.vertices._head
        while temp_node.next is not None:
            if self._is_adjacent(curr_node, temp_node.data_obj):
                adjacentNodesList.insert(temp_node.data_obj)
            temp_node=temp_node.next
        # check for the last not
        if self._is_adjacent(curr_node, temp_node.data_obj):
            adjacentNodesList.insert(temp_node.data_obj)
        
        return adjacentNodesList

    def get_edges_list_pk(self, pk):
        """
        Function to get all adjacent nodes to given node
        """
        adjacentNodesList = LinkedList()

        temp_node=self.edges._head
        while temp_node.next is not None:
            if temp_node.data_obj.get_symbol==pk:
                adjacentNodesList.insert(temp_node.data_obj)
            temp_node=temp_node.next
        # check for the last not
        if temp_node.data_obj.get_symbol==pk:
            adjacentNodesList.insert(temp_node.data_obj)
        
        return adjacentNodesList

    # Graph traversal
    def dfs(self, source, dest, visited, path):
        """
        DFS function for the graph
        """
        if path.find(source):
            print("This is already found: {0}".format(source.get_symbol))
            return
        visited.insert(source)
        path.insert(source)

        if source==dest:
            # print(path)
            # self.list_paths.insert(path)
            self.list_paths.insert(deepcopy(path))
        else:
            adjacentList=self.get_adjacent(source)
            temp=adjacentList._head
            # Entire looping through each nodes
            if adjacentList.length>0:
                while temp.next is not None:
                    if not visited.find(temp.data_obj):
                        self.dfs(temp.data_obj, dest, visited, path)
                    temp=temp.next
                if not visited.find(temp.data_obj):
                    self.dfs(temp.data_obj, dest, visited, path)
            # Entire looping ends
        
        path.remove_last()
        visited.remove(source)

    def print_paths(self):
        if self.list_paths.length==0:
            print("No paths yet...")
            return
        
        temp=self.list_paths._head
        print(temp.data_obj.print_same_line())
        # # search until end of list
        while temp.next is not None:
            print(temp.next.data_obj.print_same_line())
            temp=temp.next