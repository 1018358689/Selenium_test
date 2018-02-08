#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from lxml.html import etree

url = 'https://www.baidu.com/'
# res = requests.get(url=url).content
# dom_tree1 = etree.HTML(res)
# text1 = dom_tree1.xpath('//a[@name="tj_trnews"]/text()')[0]
# print(text1)

driver = webdriver.Chrome()
driver.get(url=url)
driver.implicitly_wait(3)
# print(driver.page_source)
# dom_tree2 = etree.HTML(driver.page_source)
# text2 = dom_tree1.xpath('//a[@name="tj_trnews"]/text()')[0]
# print(text2)
# ele = driver.find_elements_by_xpath('//a[@name="tj_trnews"]')[0].text
# print(ele)
ele_text = driver.find_element_by_id('kw')
ele_text.clear()
ele_text.send_keys('11')
ele_click = driver.find_element_by_id('su')
ele_click.click()
cookies = driver.get_cookies()
print(cookies)
driver.close()