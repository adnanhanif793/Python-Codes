'''
Created on 11-Sep-2018

@author: adnan.hanif
'''
# Strings


City= "Newjersey"

cityone="California"

print(City[0])

print (City[3]) #single character

print(City[3:9]) #substring

print(City + cityone) #Concatenation



# Lists

lists =[1,2,4,5,6,"hello"]

lists.append(9)

lists.append(2)

lists.append(2)

print (lists)

print(lists.count(2))

print(lists.count(4))

print(lists.index(5))

lists.remove(6)

print(lists)

lists.remove(2) # for removing the value

print(lists.count(2))

lists.reverse()

print(lists)