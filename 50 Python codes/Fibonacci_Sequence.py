'''
Created on 12-Dec-2019

@author: adnan.hanif
'''
from sys import breakpointhook

#Program to display fibonacci sequence till nth term

nterms=int(input("Enter term till which u want fibonacci sequence"))
n1=0
n2=1
count=0

#check if number of terms is valid
if nterms<=0:
    print("Please enter a positive number")
elif nterms==1:
    print("fibonacci sequence upto",nterms,":")
    print(n1)
else:
    print("fibonacci sequence upto",nterms,":")
    while count<nterms:
        print(n1,end=',')
        nth=n1+n2
        n1=n2
        n2=nth
        count+=1