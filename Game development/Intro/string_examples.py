'''
Created on 15-Sep-2018

@author: dell
'''
name='adnan hanif'

#name[1]='r' will give error because string are immutable in python
print("hey! i am {}".format(name))
#print("hey! i am %s", %s name)

print(name.count('n'))
print(name.lower())
print(name.upper())
print(name.capitalize()) # capitalize only first letter of first word
print(name.title()) #capitalize first letter of al words
print(name.islower())
print(name.isupper())
print(name.isalpha())#  wll return false because of the space
print('abc'.isalpha())
print('123'.isdigit())

print(name.index('n'))
#print(name.index('naa'))# will return error because it is not present in string
print(name.index('d'))

name1=input("what is your name?").strip()#removes space from beginning and end
print(len(name1))

age=input("what is your age").strip()
print("my name is {} and age is {}".format(name1,age))

