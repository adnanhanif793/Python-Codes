'''
Created on 16-Aug-2018

@author: adnan.hanif
'''
import unittest

def add(a,b):
    return(a+b)

class MytestClass(unittest.TestCase):
    def test_one(self): # name should start with test otherwise it will not be considered as test
        self.assertEqual(add(6, 5), 11, 'Passed')
    
    def test_two(self):
        try:
            self.assertEqual(add(6, 5), 12, 'Not correct')    
        except Exception as ex:
            print('Failed because the answer is' + str(ex))   
if __name__=='_main_':
    unittest.main()      