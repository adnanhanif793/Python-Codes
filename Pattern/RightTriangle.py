'''
Created on 22-May-2019

@author: adnan.hanif
'''

n = int(input("Enter number of rows:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()   
    
    
 
# Alternate way   
n1 = int(input("Enter number of rows:"))
for i in range(1,n1+1):
    print("* " * i) 