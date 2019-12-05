'''
Created on 11-Oct-2018

@author: adnan.hanif
'''
from selenium import webdriver

driver=webdriver.Chrome()
driver.get('https://accounts.google.com/SignUp?hl=en')
driver.maximize_window()

driver.find_element_by_link_text("Help").click()
print("Before Switching")
parent=driver.current_window_handle  #id of current window
#parent=driver.window_handles[0]
print(driver.title)
driver.switch_to_window(driver.window_handles[1]) #next window which opened(sequence,like 1,2)
print("After Switching")
print(driver.title)
print("switching back to parent window")
driver.switch_to_window(parent)
print(driver.title)

driver.find_element_by_link_text("Privacy").click()
driver.switch_to_window(driver.window_handles[2]) #-1 can also be given which will give the id of latest window which got opened

print(driver.title)
