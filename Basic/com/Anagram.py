'''
Created on 18-Mar-2019

@author: adnan.hanif
'''

def check(s1, s2): 
      
    # the sorted strings are checked  
    if(sorted(s1)== sorted(s2)): 
        print("The strings are anagrams.")  
    else: 
        print("The strings aren't anagrams.")          
          
# driver code   
n=int(input("Enter the number of terms"))
i=0
while(i<n):
    s1 =input("enter first")
    s2 =input("enter second")
    check(s1, s2)