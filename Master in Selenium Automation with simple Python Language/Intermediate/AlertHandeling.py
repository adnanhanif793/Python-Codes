'''
Created on 28-Sep-2018

@author: adnan.hanif
'''
from selenium import webdriver

driver=webdriver.Firefox()

driver.get("http://www.tizag.com/javascriptT/javascriptalert.php")

driver.find_element_by_xpath("//div[@class='display']/form/input").click()

print(driver.switch_to_alert().text)

driver.switch_to_alert().accept()

#driver.switch_to_alert().dismiss()

#driver.switch_to_alert().send_keys("adafds")#in case when alert has option to edit

