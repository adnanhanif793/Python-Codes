'''
Created on 05-Dec-2019

@author: adnan.hanif
'''
n=input("Enter string")
rev=[]
i=len(n)-1
while(i>=0):           
    rev.append(n[i])
    i-=1

print("".join(rev)) 


'''
#Alternate code
n=input("Enter string")
rev=""
i=len(n)-1
while(i>=0):           
    rev+=n[i]
    i-=1

print(rev) 
'''