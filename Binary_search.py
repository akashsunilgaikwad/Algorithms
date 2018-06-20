# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 01:56:22 2018

Binary Search on Sorted array 

@author: Akash
"""

import math

def Binary_search(arr,key):
    low =0
    high =len(arr)-1
    while(low<=high):
        mid = math.floor((low+high)/2) 
        if(key<arr[mid]):
            high = mid-1            
        elif (key>arr[mid]):
            low = mid+1        
        else :
            return mid
    return -1

arr = [0,1, 3, 5, 6, 11, 13, 20]
arr.sort()
print(arr)
rank = Binary_search(arr, 20)
print("The Rank is ",rank+1)

'''Rank Indexed at one'''
