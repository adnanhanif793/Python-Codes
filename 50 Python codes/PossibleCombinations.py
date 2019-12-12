'''
Created on 12-Dec-2019

@author: adnan.hanif
'''


#Program to accept 3 distinct digits and print all possible combinations from the digits
#Same can be used for string with some changes

a=int(input("Enter first digit"))
b=int(input("Enter second digit"))
c=int(input("Enter third digit"))
d=[]
if(a!=b!=c):
    d.append(a)
    d.append(b)
    d.append(c)
    for i in range(0,3):
        for j in range(0,3):
            for k in range(0,3):
                if(i!=j&j!=k&k!=i):
                    print(d[i],d[j],d[k])
else:
    print("Enter different digits")