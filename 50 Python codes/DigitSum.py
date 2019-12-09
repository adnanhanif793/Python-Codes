'''
Created on 09-Dec-2019

@author: adnan.hanif
'''
#Sum of digits

n= int(input("Enter a number"))
tot=0

while n>0:
    dig=n%10
    tot+=dig
    n=n//10

print("The sum of digits is",tot)