'''
Created on 26-Sep-2018

@author: dell
'''
class Person():
    def __init__(self,name,score):
        self.name=name
        self.score=score
    
    def info(self):
        print("I am {} and my score is {}".format(self.name, self.score))
class Mary(Person):
    def __init__(self,name,score):
        self.name=name
        self.score=score
 
class John():
    def __init__(self,name,score):
        self.name=name
        self.score=score
    
 
mary=Mary("Mary",4200)
mary.info()

john=John("John",4100)#since John does not inherit from Person, it can not use info()
john.info()
