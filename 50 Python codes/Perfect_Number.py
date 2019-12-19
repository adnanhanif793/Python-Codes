'''
Created on 18-Dec-2019

@author: adnan.hanif
'''

'''
A number is Perfect number if it is equal to sum of its factors
eg. 6=1+2+3    ,28,496

'''

n=int(input("Enter any number"))
sum1=0
for i in range(1,n):
    if(n%i==0):
        sum1+=i

if sum1==n:
    print("Number is Perfect Number")
else:
    print("Number is not perfect Number")