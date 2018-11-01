'''
Created on 16-Sep-2018

@author: dell
'''

list=[]
while len(list)<3:
    new_name=input("Enter your name").strip().title()
    list.append(new_name)
print(list)
print("list is full")