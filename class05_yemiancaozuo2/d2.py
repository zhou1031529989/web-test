# -*- coding: utf-8 -*-
# @Time     : 2020/3/21 21:31
# @Author   : Zhou_Chao
# @Email    : 1031529989@qq.com
# @File     : d2.py
# @Software : iframe
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
# 摄像头
driver.implicitly_wait(30)

driver.get("https://www.ketangpai.com/User/login.html")

# 点击 微信登录
WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"//a[text()='微信登录']"))).click()

# 找到iframe,通过iframe切换进来后，找到微信登录
ele = driver.find_element_by_tag_name('iframe')
# 等待
WebDriverWait(driver,30).until(EC.frame_to_be_available_and_switch_to_it((By.TAG_NAME,'iframe')))
# driver.switch_to.frame(ele)
time.sleep(3)
wx = driver.find_element_by_xpath("//div[@class='title']")
print(wx.text)

# 退出到主页面
driver.switch_to.default_content()
# 回到上一层
driver.switch_to.parent_frame()



