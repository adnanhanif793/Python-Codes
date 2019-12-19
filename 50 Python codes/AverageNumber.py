'''
Created on 05-Dec-2019

@author: adnan.hanif
'''
# Calculate Average of numbers in a given list

from builtins import int
n= int(input("Enter number of elements"))
a=[]
for i in range(0,n):
    elem=int(input("enter element:"))
    a.append(elem)
avg=sum(a)/n
print("Average of elements in list is:",round(avg,2))