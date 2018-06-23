# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 18:51:59 2018

@author: Akash
"""

class Node:
    
    def __init__(self, data=None, next_node=None):
        
        self.data = data
        self.next = next_node
    
    def get_data(self):
        return self.data
    
    def get_next(self):
        return self.next
    
    def set_next(self, new_node):
        self.next = new_node
        
    def traverse(self):
        
        node = self
        
        while node != None:
            print(node.data)
            node = node.next
            
class Linked_List:
    
    def __init__(self):
        
        self.head = None
    
    def insert(self, data):
        
        new_node = Node(data)        
        new_node.set_next(self.head)
        self.head = new_node
    
    def size(self):
        current_node = self.head
        count = 0
        while current_node:
            count +=1
            current_node = current_node.get_next()
        return count
    
    def search(self, data):
        
        current_node = self.head
        found = False
        while current_node and found is False:
            if current_node.get_data() == data:
                found = True
            else:
                current_node = current_node.get_next()
        if current_node is None:
            raise ValueError("Data not in the list")
        return found
    
    def print_list(self):
        
        current_node = self.head
        linked_list = list()
        while current_node:
            linked_list.append(current_node.get_data())
            current_node = current_node.get_next()
        return linked_list
    
    def delete(self, data):
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                previous = current
                current = current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())
            
    
#node1 = Node(12)
#node2 = Node(15)
#node3 = Node(63)
#
#node1.next = node2
#node2.next = node3
#
#node1.traverse()
linked_list = Linked_List()
linked_list.insert(23)
linked_list.insert(50)
print(linked_list.size())
print(linked_list.search(50))
print(linked_list.print_list())
print(linked_list.delete(50))
print(linked_list.size())
print(linked_list.print_list())




        