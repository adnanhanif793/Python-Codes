'''
Created on 26-Sep-2018

@author: dell
'''
import pickle
 
class account:
    def __init__(self, id, balance):
        self.id = id
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        self.balance -= amount
 
myac = account('123', 100)
myac.deposit(800)
myac.withdraw(500)
 
fd = open( "archive", "wb" ) #pickling is storing data in file ffor later use
pickle.dump( myac, fd)#pickle will store the state of the account object to file when its value is 400. After storing the value to file 200 is added and 600 is printed. After printing 600 the object form file is reloaded from file and printed with a value of 400.
fd.close()
 
myac.deposit(200)
print(myac.balance)
 
fd = open( "archive", "rb" )#unpickling is loading data saved in a file 
myac = pickle.load( fd )
fd.close()
 
print(myac.balance)


