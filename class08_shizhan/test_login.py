# -*- coding: utf-8 -*-
# @Time     : 2020/3/23 13:06
# @Author   : Zhou_Chao
# @Email    : 1031529989@qq.com
# @File     : 163.py
# @Software :

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from class8_shizhan.pages.login_page import LoginPage


class TestLogin(unittest.TestCase):

    def setUp(self):
        # 创建写入测试的实例
        # self.t = DoExcel()
        self.driver = webdriver.Chrome()
        self.driver.get('http://120.78.128.25:8765/Index/login.html')
        self.driver.maximize_window()
        self.login_page = LoginPage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_login_1_failed(self):
        # 访问登录页面
        self.login_page.submit_userinfo("","")
        # 等待
        flash_msg_ele = WebDriverWait(self.driver,30).until(
            EC.visibility_of_element_located((By.XPATH,"//div[@class='form-error-info']"))
        )
        # 断言
        self.assertTrue('请输入手机号' == flash_msg_ele.text)

    def test_login_2_success(self):
        self.login_page.submit_userinfo("18684720553","python")

        user_ele = WebDriverWait(self.driver,20).until(
            EC.visibility_of_element_located((By.XPATH,"//img[@class='mr-5']//.."))
        )
        self.assertIn('python',user_ele.text)

if __name__ == "__main__":
    unittest.main()















