'''
Created on 07-Aug-2018

@author: adnan.hanif
'''
from selenium.webdriver.common.action_chains import ActionChains

from selenium import webdriver

driver=webdriver.Chrome()
driver.maximize_window()
driver.get('https://jqueryui.com/droppable/')
driver.implicitly_wait(3)
driver.switch_to_frame(0)
source=driver.find_element_by_id('draggable')
target=driver.find_element_by_id('droppable')
 
ActionChains(driver).drag_and_drop(source, target).perform()
