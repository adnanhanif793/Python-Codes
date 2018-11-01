'''
Created on 16-Sep-2018

@author: dell
'''
new_list=['Adnan','Hanif',1,3,True]
print(new_list)
print(type(new_list))
new_list.reverse() #permanently reverses the original list
print(new_list)

new_list=new_list[::-1]
print(new_list)

print(new_list[1])
print(new_list[-1])
print(new_list[:2:])
print(new_list[2:4:])

our_list=[1,2,[3,4,5],[6,7]]
print(our_list[2])
print(our_list[2][1])
print(our_list[::-1])#doesn't reverses the original list

our_list.append('item')
print(our_list)

a=our_list.pop(4) #pop return the removed element from index,if not specified then last element
print(a)
print(our_list)

our_list.remove([6,7]) #remove, removes element with value equal to given in paranthese
print(our_list)
our_list.reverse()
print(our_list)
print(len(our_list))