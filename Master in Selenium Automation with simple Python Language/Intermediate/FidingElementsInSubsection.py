'''
Created on 01-Oct-2018

@author: adnan.hanif
'''
from selenium import webdriver

driver=webdriver.Firefox()

driver.get("http://www.amazon.in")

# no of links present in Website ebay home page

totallinks=driver.find_elements_by_tag_name("a")

print(len(totallinks))

footer=driver.find_element_by_xpath("//*[@id='navFooter']")

#no. of links present in the footer
linksfooter=footer.find_elements_by_tag_name("a")

print(len(linksfooter))

for ob in linksfooter :

    print(ob.text)
    
driver.quit()