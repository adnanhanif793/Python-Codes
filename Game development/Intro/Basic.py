'''
Created on 15-Sep-2018

@author: dell
'''
import math
from math import ceil, floor

print("adnan")

a,b=5,2.5
print(a**2.0)
print(pow(a,3))
print(a%2)
print(a/2)
print(ceil(b))
print(floor(b))
print(math.pi)

print(type(a))

print(min('hello world')) #python considers a blank space character as minimum value in a string
print(min('Hello')) # and in case of no blank space the alphabet which comes first, like e comes before other alphabets in the word,looks like on ASCII character
print(type(type(int))) # type function returns the class of the argument the object belongs to. Thus, type returns which is of the type 'type' object.


print(0.1+0.2==0.3) # Neither of 0.1, 0.2 and 0.3 can be represented accurately in binary. The round off errors from 0.1 and 0.2 accumulate and hence there is a difference of 5.5511e-17 between (0.1 + 0.2) and 0.3.