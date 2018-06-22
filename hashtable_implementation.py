# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 16:16:11 2018

@author: Akash
"""

class Hashtable():
    
    def __init__(self):
        self.table = [None]*256
#        print(self.table)
        
    def hash_function(self, data):
        
        total = 0
        for i in range(len(data)):
            total += ord(data[i]) * (7**i)
        index = (total * len(data))%256
        return index
        
    def insert(self, data):
        
        index = self.hash_function(data)
        
        if self.table[index] == None:
            self.table[index] = data
        else:
            if type(self.table[index]) == list:
                self.table[index].append(data)
            else:
                self.table[index] = [self.table[index], data]
    
    def delete(self,data):
        
        index = self.hash_function(data)
        
        if self.table[index] != None:
            if type(self.table[index]) == list:
                i = self.table[index].index(data)
                self.table[index][i] = None
            else:
                self.table[index] = None
            
        else:
            print("Key Error")
            
            
    def lookup(self, data):
        found = False
        index = self.hash_function(data)
        if type(self.table[index]) == list:
            found = data in self.table[index]
            return found
        else:
            found = (self.table[index] == data)
        return found 
        
        
obj = Hashtable()

obj.insert("akash")
obj.insert("akash")
obj.insert("ragi")
obj.insert("alisha")
print(obj.lookup("akash"))
obj.delete("akash")
obj.delete("akash")
print(obj.lookup("akash"))

print(obj.table)
