'''
Created on 16-Sep-2018

@author: dell
'''
for i in range(1,11,2): #range will provide a list from 1 to 10
    print(i)
    
for i in "adnan":
    print(i)


print([(a,b) for a in range(3) for b in range(a)]) # since when a=0, b will not have any value as upper limit is exclusive

for a in range(3):
    for b in range(a):
        print([(a,b)])
            