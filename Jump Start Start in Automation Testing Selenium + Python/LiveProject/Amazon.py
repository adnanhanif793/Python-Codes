'''
Created on 27-Aug-2018

@author: adnan.hanif
'''

from selenium import webdriver

driver=webdriver.Chrome()

driver.get('http://amazon.in')


total_links=driver.find_elements_by_tag_name('a')

print(len(total_links))

footer=driver.find_element_by_xpath("//*[@id='navFooter']")
footerLinks=footer.find_elements_by_tag_name('a')

print(len(footerLinks))

for links in footerLinks:
    print(links.text)
driver.quit()