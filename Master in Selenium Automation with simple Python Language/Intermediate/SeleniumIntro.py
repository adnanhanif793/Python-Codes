'''
Created on 25-Sep-2018

@author: adnan.hanif
'''

from selenium import webdriver
import time
driver=webdriver.Chrome()# if path of chromedriver is not set in environment variable, pass here
driver.maximize_window()

driver.get('https://smtlogin.zycus.net/sso/login')
print(driver.current_url)
print(driver.title)

print("Navigating to google")
driver.get('https://google.com')
print(driver.title)
driver.back()
print(driver.title)
driver.forward()
print(driver.title)

driver.refresh()

#driver.close() # Closes the current window.
driver.quit() # Closes all the windows and shuts down the webdriver

time.sleep(5)