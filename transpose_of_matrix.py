# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 17:08:24 2018

@author: Akash
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 00:13:47 2018

@author: Akash

Transpose_of_matrix

"""

def Transpose_of_matrix(arr, row, column):
    new_matrix = []
    
    for i in range(column):
        new_row = []
        for k in range(row):
            new_row.append(arr[k][i])
#            print(new_row)
        new_matrix.append(new_row);
    return new_matrix
    

#matrix_dim = list(map(int, input().split()))
#row = matrix_dim[0]
#column = matrix_dim[1]
#
#matrix = []
#for i in range(row):
#    matrix.append(list(map(int,input().split())))

matrix = [[13 ,4, 8, 14, 1],[9, 6, 3, 7, 21],[5 ,12, 17, 9 ,3]]
print(matrix)
row = 3
column = 5 
new_matrix = Transpose_of_matrix(matrix, row, column)
print(new_matrix)
#print(len(new_matrix))

for i in range(len(new_matrix)):
    L = list(map(str,new_matrix[i]))
    print(" ".join(map(str, L)))