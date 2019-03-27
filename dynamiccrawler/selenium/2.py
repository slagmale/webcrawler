from selenium import webdriver
from selenium.webdriver.common.by import By
import time

'''
节点交互
'''
browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
input = browser.find_element_by_id('q')
input.send_keys('iPhone')
time.sleep(1)
input.clear()
input.send_keys('iPad')
#button = browser.find_element_by_class_name('btn-search')
button = browser.find_element(By.CLASS_NAME,'btn-search')
button.click()