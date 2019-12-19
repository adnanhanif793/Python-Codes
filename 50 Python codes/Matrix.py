'''
Created on 19-Dec-2019

@author: adnan.hanif
'''
'''
Program for matrix input from user and display same in matrix format
'''

r=int(input("Enter number of rows of matrix"))
c=int(input("Enter number of columns of matrix"))

matrix=[]

for i in range(r):
    a=[]
    for j in range(c):
        a.append(int(input()))
    matrix.append(a)

for i in range(r):
    for j in range(c):
        print(matrix[i][j],end=" ")
    print()