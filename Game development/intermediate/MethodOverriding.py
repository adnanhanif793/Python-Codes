'''
Created on 27-Sep-2018

@author: dell
'''

class Parent:
    def myMethod(self):
        print('calling parent method')
        
    
class Child(Parent):
    def myMethod(self):
         print('calling child method')
         #Parent.myMethod(self)
        
c=Child()
c.myMethod()