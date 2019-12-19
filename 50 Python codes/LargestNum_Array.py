'''
Created on 19-Dec-2019

@author: adnan.hanif
'''

'''
Find maximum element in an array
'''

def largest(arr,n):
    max=arr[0]
    
    for i in range(1,n):
        if arr[i]>max:
            max=arr[i]
    return max
    
arr=[3,32,7,12,91]
n=len(arr)
result=largest(arr,n)
print("largest number in the list is",result)
