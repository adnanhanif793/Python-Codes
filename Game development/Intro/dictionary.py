'''
Created on 16-Sep-2018

@author: dell
'''
emp={
     'Mary':24,
     'Dan':32,
     'Clara':21
     }
 
print(emp)

print(emp['Mary'])
print(emp['Clara'])

emp['Ethan']=35
emp['Dan']=38
print(emp)

del emp['Dan']
print(emp)

print(emp.keys())
print(emp.values())
a=list(emp.keys()) #converting a dictionary into list
b=list(emp.values())# dictionary has to be converted to list for indexing
print(a,b)

print(a[1],b[1])

#converting dictionary to tuples as they are more manageable,indexable and iterable
print(emp.items())
c=tuple(emp.items())
print(c)
