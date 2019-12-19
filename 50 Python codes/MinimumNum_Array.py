'''
Created on 19-Dec-2019

@author: adnan.hanif
'''

'''
Find minimum element in an array
'''

def smallest(arr,n):
    min=arr[0]
    
    for i in range(1,n):
        if arr[i]<min:
            min=arr[i]
    return min
    
arr=[3,32,7,12,91]
n=len(arr)
result=smallest(arr,n)
print("smallest number in the list is",result)