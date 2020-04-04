# -*- coding: utf-8 -*-
# @Time     : 2020/3/23 15:11
# @Author   : Zhou_Chao
# @Email    : 1031529989@qq.com
# @File     : login_page.py
# @Software : Login页面属性与方法

import time
class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def submit_userinfo(self, phone, pwd):
        phone_ele = self.driver.find_element_by_name('phone')
        pwd_ele = self.driver.find_element_by_name('password')

        # 提交信息
        phone_ele.send_keys(phone)
        pwd_ele.send_keys(pwd)
        phone_ele.submit()

        time.sleep(5)

    def remember_me(self):
        pass