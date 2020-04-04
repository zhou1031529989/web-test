# -*- coding: utf-8 -*-
# @Time     : 2020/3/21 18:02
# @Author   : Zhou_Chao
# @Email    : 1031529989@qq.com
# @File     : d2.py
# @Software : 
from selenium import webdriver

driver = webdriver.Chrome()

driver.get("http://baidu.com")

ele = driver.find_element_by_xpath("//input[@id='kw']")
print(ele)  # 一个元素，WebElement对象
print(ele.text)  # 打印内容
print(ele.tag_name)  # 查找属性 tag_name 就是input（通过input查找的）
print(ele.get_attribute('name'))  # 查找某一个元素属性，即查找ele元素name属性的值
# set改变元素的属性，只有js可以做，python如果要做，就要发命令给js，让js去做
# 查找他的子元素
# ele.find_element_by_xpath()

# 输入内容
ele.send_keys("差不多先生")
# 点击百度一下
driver.find_element_by_id("su").click()
# 等待
import time
time.sleep(2)
# 再输入其他内容
ele.clear()
ele.send_keys("冰冰")
driver.quit()

