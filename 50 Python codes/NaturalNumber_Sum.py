'''
Created on 18-Dec-2019

@author: adnan.hanif
'''
'''
program to add all natural numbers

sum=1+2+3+...+n
'''

n=int(input("Enter n:"))

sum=0
i=1

while i<=n:
    sum=sum+i
    i+=1
    
print("The sum of all natural numbers from 1 to {}".format(n),"is",sum)