'''
Created on 27-Sep-2018

@author: dell
'''
class Vector:
    def __init__(self,a,b):
        self.a=a
        self.b=b
        
    def __str__(self): #__str__ is the built-in function in python, used for string representation of object
         return 'Vector ({},{})'.format(self.a,self.b)
         #return 'Vector (%d,%d)'%(self.a,self.b) 
        
    def __add__(self,other): #for vector addition
        return Vector(self.a+other.a,self.b+other.b)


v1=Vector(1,5)
v2=Vector(-10,2)

print(v1+v2)



        