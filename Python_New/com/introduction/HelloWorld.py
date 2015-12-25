'''
Created on Dec 24, 2015

@author: PARAMESH MARINA
'''
print ("hi selenium")

from selenium import webdriver

driver =webdriver.Firefox()
driver.get("http://www.google.com/")
driver.quit()
print(driver.current_url())
print(driver.page_source())
print(driver.title())
driver.close()
driver.back()
driver.forward()
driver.title()
driver.refresh()

driver.maximize_window()




