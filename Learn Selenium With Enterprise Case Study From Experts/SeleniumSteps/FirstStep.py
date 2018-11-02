'''
Created on 16-Aug-2018

@author: adnan.hanif
'''

from selenium import webdriver
import time
try:
    driver=webdriver.Chrome()
    driver.get("http://ui5cn.com")
    time.sleep(2)
except Exception as ex:
    print("error!" + str(ex))
    
else:
    print("Title is "+ driver.title)
    time.sleep(3)  
    
finally:
    driver.quit()