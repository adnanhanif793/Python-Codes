'''
Created on 09-Aug-2018

@author: adnan.hanif
'''
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

'''DesiredCapabilities={}
DesiredCapabilities['platform']='Windows'
DesiredCapabilities['browser']='Firefox'
DesiredCapabilities['browser']='Chrome'''
#working without desired capabilities also
driver=webdriver.Firefox()
driver.get("http://google.com")

driver=webdriver.Chrome()
driver.get("http://google.com")