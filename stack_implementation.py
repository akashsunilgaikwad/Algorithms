# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 19:10:03 2018

Stack Implementation 

@author: Akash
"""

class Stack:
    
    def __init__(self):
        self.stack = list()
    
    def push(self,data):
        
        if data not in self.stack:
            self.stack.append(data)
            return True
        return False 
    
    def pop(self):
        if len(self.stack)<=0:
            return ("stack empty")
        return self.stack.pop()
        
    def size_stack(self):
        return len(self.stack)
    
        
myStack = Stack()

print(myStack.push(5)) #prints True
print(myStack.push(6)) #prints True
print(myStack.push(9)) #prints True
print(myStack.push(5)) #prints False since 5 is there
print(myStack.push(3)) #prints True
print(myStack.size_stack())  #prints 4 
print(myStack.pop())   #prints 3
print(myStack.pop())   #prints 9
print(myStack.pop())   #prints 6
print(myStack.pop())   #prints 5
print(myStack.size_stack())  #prints 0
print(myStack.pop())   #prints Stack Empty!