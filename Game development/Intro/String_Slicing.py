'''
Created on 15-Sep-2018

@author: dell
'''
info='hi i am computer engineer'
print(info[8:16:])
print(info[:16:])
print(info[8::])
print(info[8:16:2])# print alternate letters
print(info[8:16:3])# prints skipping 2 letters
print(info[15:7:-1])# since it is -1 it will start in reverse
print(info[8::-1])
print(info[:16:-1])
print(info[::-1])
print(info[::-2])

email=input('Enter your email id ')
if(email.__contains__('@') & email.__contains__('.')):
    
    username=email[:email.index('@'):]#before @ everything will be username
    domain=email[email.index('@')+1:email.index('.'):]#after @ till . is domain

    print('your username is {} and domain is {}'.format(username, domain))
else:
    print('invalid email id')
       