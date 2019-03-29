'''
Created on 30-Jul-2018

@author: adnan.hanif
'''
from selenium import webdriver

driver= webdriver.Chrome()
#driver = webdriver.Firefox(executable_path='C:/Users/adnan.hanif/Desktop/geckodriver.exe')
driver.get("http://google.co.in")
print(driver.current_url)
print(driver.title)
driver.maximize_window()
driver.save_screenshot("C:/Users/adnan.hanif/Desktop/google.png")
driver.get("http://bing.com")
driver.save_screenshot("C:/Users/adnan.hanif/Desktop/bing.png")
print(driver.title)
driver.back()
print(driver.title)
driver.forward()
print(driver.title)

driver.refresh()
driver.close()
driver.quit()
