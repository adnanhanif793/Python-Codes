'''
Created on 09-Dec-2019

@author: adnan.hanif
'''
#Check if  a number is Palindrome or not

n= int(input("Enter a number"))
temp=n
rev=0

while n>0:
    dig=n%10
    rev=rev*10+dig
    n//=10

if temp==rev:
    print("Palindrome")

else:
    print("Not Palindrome")
    