'''
Created on 16-Oct-2018

@author: adnan.hanif
'''
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains



#from selenium.webdriver.common.keys import Keys # will get imported automatically on pressing ctrl+c twice

driver= webdriver.Chrome()
driver.maximize_window()
driver.get('http://google.com')
search=driver.find_element_by_xpath("//*[@id='gs_htif0']")

#context click is used for right click
ActionChains(driver).move_to_element(search).context_click(search).perform()


#driver.find_element_by_xpath("//input[@id='lst-ib']").send_keys(Keys.SHIFT,'afddsg') #for entering capital letters

