# -*- coding: utf-8 -*-
# @Time     : 2020/3/23 15:11
# @Author   : Zhou_Chao
# @Email    : 1031529989@qq.com
# @File     : login_page.py
# @Software : Login页面属性与方法

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from class10_invest.pages.base import BasePage



class LoginPage(BasePage):
    # toast提示定位器
    flash_msg_locator = (By.XPATH, "//div[@class='form-error-info']")
    # 描红提示定位器
    alert_locator = (By.XPATH, "//div[@class='layui-layer-content']")
    # 手机号码定位器
    phone_locator = (By.NAME, 'phone')
    # 密码定位器
    pwd_locator = (By.NAME, 'password')

    def submit_userinfo(self, phone, pwd):
        phone_ele = self.driver.find_element_by_name('phone')
        pwd_ele = self.driver.find_element_by_name('password')

        # 输入内容
        phone_ele.send_keys(phone)
        pwd_ele.send_keys(pwd)
        # 提交信息
        phone_ele.submit()

        # 等待5s后，未授权账户的toast提示，就将消失
        # time.sleep(5)

    def alert_info(self):
        # return self.driver.find_element_by_xpath("//div[@class='form-error-info']")

        return WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.flash_msg_locator)
        )

    def unauthorized_info(self):

        # self.driver.find_element_by_xpath("//div[@class='layui-layer-content']")
        return WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.alert_locator))

    def clear_phone(self):
        return self.get_phone_element().clear()

    def clear_pwd(self):
        return self.get_pwd_element().clear()

    def get_phone_element(self):
        return self.get_visible_element(self.phone_locator)

    def get_pwd_element(self):
        return self.get_visible_element(self.pwd_locator)

    def remember_me(self):
        pass