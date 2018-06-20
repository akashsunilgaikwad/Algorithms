# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 17:06:02 2018
The Selection sort algorithm is based on the idea of finding the minimum or
 maximum element in an unsorted array and then putting 
 it in its correct position in a sorted array.
@author: Akash
"""
def swap(num1,num2):
    temp = num1
    num1=num2
    num2 = temp
    return num1, num2
    

def selection_sort(arr):
    
   for counter in range(len(arr)):
       minimum = counter
       for i in range(counter, len(arr)):
           if (arr[i]<arr[minimum]):
               minimum = i
       arr[minimum],arr[counter] = swap(arr[minimum],arr[counter])
   print(arr)             
   
                
arr =[6, 65, 9, 3 ,56 , 77 , 0 , 21, 1, 2]
print("Original array: ",arr)
selection_sort(arr)


