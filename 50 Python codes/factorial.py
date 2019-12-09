'''
Created on 05-Dec-2019

@author: adnan.hanif
'''

#Factorial

from math import factorial
from test.test_buffer import prod

def factorial(n):
    if(n==1  or n==0):
        return 1
     
    else:
        return n*factorial(n-1)
        #return(prod(range(1,n+1)))
     
num=int(input("Enter number"))
print("Factorial of",num,"is",factorial(num))

# fact(num)
