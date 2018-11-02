'''
Created on 12-Oct-2018

@author: adnan.hanif
'''
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains #To perform Mouse movement actions
# Use action class whenever u see ul->li tags

driver=webdriver.Chrome()
driver.get('https://www.spicejet.com/')
driver.maximize_window()
menu=driver.find_element_by_xpath("//span[contains(text(),\"MENU\")]")
ActionChains(driver).move_to_element(menu).perform()

travelInfo=driver.find_element_by_xpath("//li[@class='hide-mobile']/a[contains(text(),'Travel Info')]")
time.sleep(3)

ActionChains(driver).move_to_element(travelInfo).perform()