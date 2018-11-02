'''
Created on 28-Sep-2018

@author: adnan.hanif
'''
from selenium import webdriver
#import time

#chromedriverpath= "C:\chromedriver.exe"

driver=webdriver.Chrome()#chromedriverpath to be passed here

driver.get("https://paytm.com/")
driver.maximize_window()
#driver.find_element_by_xpath('//input[@data-reactid="194"]').click()

driver.find_element_by_xpath('//input[@data-reactid="194"]').send_keys("8953722689")
#time.sleep(2)
driver.find_element_by_xpath('//input[@data-reactid="217"]').send_keys("400")

#Css Selector * means contains in CSS
driver.find_element_by_css_selector('button[class*="3y9b"]').click()
#tag[starts-with(@attr, 'value')]