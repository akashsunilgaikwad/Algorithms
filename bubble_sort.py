# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 02:26:16 2018

Bubble sort is based on the idea of repeatedly comparing pairs of adjacent elements 
and then swapping their positions if they exist in the wrong order.

@author: Akash
"""

def bubble_sort(arr):
    
    number_of_elements =len(arr)
    for k in range(number_of_elements-1):
        for i in range(number_of_elements-1-k):
            temp = arr[i]
            arr[i] = arr[i+1]
            arr[i+1] = temp
    return arr

arr =[5, 4, 3, 2, 1, 0]

new_arr = bubble_sort(arr)
print(new_arr)