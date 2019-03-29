'''
Created on 06-Aug-2018

@author: adnan.hanif
'''
from selenium import webdriver

driver= webdriver.Chrome()
driver.get('http://google.com')

driver.execute_script("window.open('http://bing.com','new window')")
driver.switch_to_window(driver.window_handles[0])
driver.implicitly_wait(7)
driver.execute_script("window.open('http://ask.com','another window')")
#driver.switch_to_window(driver.window_handles[-2])
                        