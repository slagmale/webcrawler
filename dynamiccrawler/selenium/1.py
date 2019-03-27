from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
# 访问页面
browser.get('https://www.taobao.com')
print(browser.page_source)

#查找单个节点
#搜索框的节点
first = browser.find_element_by_id('q')
second = browser.find_element_by_css_selector('#q')
third = browser.find_element_by_xpath('//*[@id="q"]')
fourth = browser.find_element(By.ID,'q')

#查找多个节点
lis = browser.find_elements_by_css_selector('.service-bd li')
lis2 = browser.find_elements(By.CSS_SELECTOR, '.service-bd li')

browser.close()


