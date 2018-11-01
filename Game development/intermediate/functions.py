'''
Created on 16-Sep-2018

@author: dell
'''

def add(x,y):
    return x+y

sum=add(3, 7)
print(sum)
print(add(5, 1))
print(add(y=5, x=10)) #with keyword argument the places can be interchanged


def rev(text):
    print(text[::-1])
    
rev('Adnan')      


def info(name,likes,age=25): #default argument should always be at last
    detail="i am {}, {} years old and i like {}".format(name,age,likes)
    print(detail)
    
info('Adnan','Java')


def noReturn(x,y):
    x=x+y #if a function does not return any value, Python explicitly defines the None object that is returned if no value is specified
    
print(noReturn(10,15))

