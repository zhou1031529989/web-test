# -*- coding: utf-8 -*-
# @Time     : 2020/3/23 13:06
# @Author   : Zhou_Chao
# @Email    : 1031529989@qq.com
# @File     : 163.py
# @Software :

import unittest

from ddt import ddt,data
from selenium import webdriver
import pytest
from class10_invest.datas import login_data
from class10_invest.pages.index_page import IndexPage
from class10_invest.pages.login_page import LoginPage


# 1.测试类要以Test开头
# 2.测试模块要你test_开头或_test结尾
# 3.测试类里面不能有__init__方法
# 4.测试方法要以test开头
@pytest.mark.all
@ddt
class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get('http://120.78.128.25:8765/Index/login.html')
        cls.driver.maximize_window()
        cls.login_page = LoginPage(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        print("*****************开始执行测试用例*******************")

    def tearDown(self):
        # 删除输入框内信息
        #     self.login_page.clear_phone()
        #     self.login_page.clear_pwd()
        # 因为登录成功后就跳转页面了，手机号和密码输入框元素就定位不到了，所以将清空操作改为刷新可令登陆成功用例执行成功
        self.driver.refresh()

    # 冒烟测试
    @pytest.mark.login
    @pytest.mark.smoke
    @data(*login_data.user_incorrect)
    def test_login_1_failed(self,data):
        # 访问登录页面
        self.login_page.submit_userinfo(data['phone'], data['password'])
        # 断言
        self.assertTrue(data['expected'] == self.login_page.alert_info().text)

    @pytest.mark.login
    @data(*login_data.user_unauthorized)
    def test_login_0_failed(self,data):
        # 访问登录页面
        self.login_page.submit_userinfo(data['phone'], data['password'])
        # 断言
        self.assertTrue(data['expected'] == self.login_page.unauthorized_info().text)

    def test_login_2_success(self):
        self.login_page.submit_userinfo('18684720553','python')
        user_ele = IndexPage(self.driver).get_user()
        self.assertTrue('华华' in user_ele.text)

if __name__ == "__main__":
    unittest.main()















