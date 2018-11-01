'''
Created on 28-Sep-2018

@author: dell
'''
import collections # data structure, alternative to list,dictionary,set and tuple
import math
import os #open the file and work with the path
import turtle
from turtle import Turtle
def path(filename):
    filepath=os.path.realpath(__file__)
    print(filepath)
    dirpath=os.path.dirname(filepath)
    print(dirpath)
    fullpath=os.path.join(dirpath,filepath)
    print(fullpath)
    return fullpath
path('adn')   

def line(a,b,x,y):
    
    Turtle.up()
    Turtle.goto(a, b)
    Turtle.down()
    Turtle.goto(x,y)
    
class vector(collections):
    PRECISION=6 #check the number and round it
    __slots__=('_x','_y','_hash') #hash is to check whether the slot is already full or not
    
    
    
    