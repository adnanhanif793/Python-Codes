'''
Created on 20-Sep-2018

@author: dell
'''

print(1,2,3,4,5) #the result we get is unpacking

num=[1,2,3,4,5]
print(num)

print(*num) #* for unpacking normal  arguments and ** for keyword arguments

print(*"Adnan hanif")


def add(*num):
    total=0
    for n in num:
        total=total+n
    return total

print(add(23+12+4+3))


def about(name,age,likes):
    info="i am {},{} years old and i like {}".format(name,age,likes)
    return info

print(about("John",32,'Python'))
print(about('John','Python',34))
print(about(name='John',likes='Python',age=28))

dict1={"name":"John","age":24,"likes":"Security"}

print(about(**dict1))

def programming(**kwargs):
    for key,value in kwargs.items():
        print("{}={}".format(key,value))
    
programming(Python='Easy',Java='Hard',C='Very Hard')
        

