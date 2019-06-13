'''
Created on 16-Sep-2018

@author: dell
'''
#program which count the number of each character in a string

dic={}

s=input("enter")
for i in s:
    dic[i]=dic.get(i, 0) +1 #get check if value is present for the key , other wise return default value which is after the comma
    
#print("\n".join(['%s=%s'%(k,v) for k,v in dic.items()])) #for can be written outside also

print('\n'.join(['{}={}'.format(k,v) for k,v in dic.items()]))


a = ['he', 'she', 'we']
print(','.join(a))  # The method join() takes list of string as input and returns string as output. It removes ', ' and add the given string with join to the list


