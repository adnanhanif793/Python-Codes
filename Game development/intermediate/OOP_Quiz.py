'''
Created on 26-Sep-2018

@author: dell
'''
class parent:
    def __init__(self, param):
        self.v1 = param
 
class child(parent):
    def __init__(self, param):
        self.v2 = param


obj = child(11)

print(obj.v1 + obj.v2) #AttributeError: child instance has no attribute 'v1'. self.v1 was never created as a variable since the parent __init__ was not explicitly called.