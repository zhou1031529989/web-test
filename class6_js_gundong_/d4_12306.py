# -*- coding: utf-8 -*-
# @Time     : 2020/3/22 16:09
# @Author   : Zhou_Chao
# @Email    : 1031529989@qq.com
# @File     : d4_12306.py
# @Software : 抢票

# JS改变标签的属性值
# e = document.getElementById("train_date")
# e.readOnly = false
# e.value = "2020-3-23"

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get('https://www.12306.cn/index/')


def find_element(locator:tuple) -> WebElement:
    """locator:定位器
     -> 动态语言，说明返回的是一个WebElement对象
     说明，locator是一个元祖
    """
    date_ele = WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located(locator))

    if not isinstance(date_ele, WebElement):
        raise Exception

    return date_ele


date_ele = find_element((By.ID, 'train_date'))
print(date_ele)

# python调用js方法一
# driver.execute_script("e = document.getElementById('train_date');e.readOnly = false;e.value = '2020-03-24';")
# time.sleep(5)

# 方法二
# # arguments[0]占位符，相当于format
# js_code = "arguments[0].readOnly = false"
# # 执行 js 代码
# driver.execute_script(js_code, date_ele)
# time.sleep(2)
# js_code = "arguments[0].value = '2020-03-23'"
# driver.execute_script(js_code, date_ele)
# time.sleep(5)

# 方法三
# js 找元素 ，中间没有加等待，容易不成功
# js_code = """e = document.getElementById('train_date');
# e.readOnly = false;
# e.value = '2019-03-12';"""
#
# driver.execute_script(js_code)
# time.sleep(5)



driver.quit()
