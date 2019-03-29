'''
Created on 13-Aug-2018

@author: adnan.hanif
'''

from selenium import webdriver

driver= webdriver.Chrome()
driver.get('http://google.com')

alert=driver.switch_to_alert()