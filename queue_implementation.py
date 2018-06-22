# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 01:50:15 2018

@author: Akash
"""

class Queue:
    
    def __init__(self):
        self.queue = list()
        
    def enqueue(self, data):
        self.queue.insert(0, data)
        return True
    
    def dequeue(self):
        return self.queue.pop()
    
    def size_queue(self):
        return len(self.queue)
    
myqueue = Queue()

print(myqueue.enqueue(10))
print(myqueue.enqueue(2))
print(myqueue.enqueue(33))
print(myqueue.queue)
print(myqueue.size_queue())
print(myqueue.dequeue())
print(myqueue.queue)

    
    