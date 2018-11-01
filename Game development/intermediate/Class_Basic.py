'''
Created on 26-Sep-2018

@author: dell
'''
class Character():
    def __init__(self,name):
        self.name=name
    
    def running(self):
        print("{} is running".format(self.name))
        

john=Character('Adnan')
john.running()

hope=Character('hope')
hope.running()