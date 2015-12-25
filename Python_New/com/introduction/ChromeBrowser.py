'''
Created on Dec 24, 2015

@author: PARAMESH MARINA
'''
chromedriverpath="C:\chromedriver.exe"

from selenium import webdriver

driver=webdriver.Chrome(chromedriverpath)

driver.get("https://www.google.co.in")
driver.find_element_by_name("paramesh")
driver.find_element_by_id(123)
driver.find_element_by_partial_link_text('paramesh')
driver.find_element_by_xpath("//*[@name='paramesh]").send_keys("pam");


