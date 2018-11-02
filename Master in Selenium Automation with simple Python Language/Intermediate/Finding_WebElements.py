'''
Created on 26-Sep-2018

@author: adnan.hanif
'''
from selenium import webdriver

driver=webdriver.Chrome()
driver.get('https://smtlogin.zycus.net/sso/login')
driver.maximize_window()
driver.find_element_by_id('emailAddressGhost').click()
driver.find_element_by_id('emailAddress').send_keys('diego.maradona@mariners.com')

driver.find_element_by_name('pass_temp').click()
driver.find_element_by_id('password').send_keys('iRequest@13')

print(driver.find_element_by_xpath("//div[@class='zyDesc']").text)
print(driver.find_element_by_id("signIn").text)
driver.find_element_by_id('signIn').click()

driver.close()