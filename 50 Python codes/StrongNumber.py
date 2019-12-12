'''
Created on 12-Dec-2019

@author: adnan.hanif
'''

# Strong numbers are numbers whose sum of factorial of digits is equal to original number
#145 is a strong number

sum1=0
num=int(input("Enter a number to be checked as strong number"))
temp=num
while num:
    i=f=1
    r=num%10
    while i<=r:
        f=f*i
        i+=1
    sum1=sum1+f
    num=num//10
if(sum1==temp):
    print(temp,"is strong number")
else:
    print(temp,"is not strong number")
    