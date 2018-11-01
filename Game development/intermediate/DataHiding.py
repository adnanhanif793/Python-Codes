'''
Created on 28-Sep-2018

@author: dell
'''
class JustCounter:
    __secretCount=0 #__ is for data hiding
    
    def count(self):
        self.__secretCount+=1
        print(self.__secretCount)
        
counter=JustCounter()
counter.count()
counter.count()

#print(counter.__secretCount)# __secretCount cannot be accessed because of data hiding

# to access data hidden variable we use this
print(counter._JustCounter__secretCount)

