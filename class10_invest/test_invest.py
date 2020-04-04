# -*- coding: utf-8 -*-
# @Time     : 2020/3/23 21:22
# @Author   : Zhou_Chao
# @Email    : 1031529989@qq.com
# @File     : test_invest.py
# @Software : 投资
"""
约束条件：已登陆 有标 有钱 标有余
"""

import unittest

from selenium import webdriver

from class10_invest.datas import login_data,bid_data
from class10_invest.pages.bid_page import BidPage
from class10_invest.pages.index_page import IndexPage
from class10_invest.pages.login_page import LoginPage


class TestInvest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://120.78.128.25:8765/Index/login.html')
        self.driver.maximize_window()
        self.login_page = LoginPage(self.driver)
        self.login_page.submit_userinfo(
            login_data.user_correct['phone'],login_data.user_correct['password']
        )
        self.bid_page = BidPage(self.driver)

    def tearDown(self):
        self.driver.quit()


    # def test_bid_send10_popup(self):
    #     # 访问登录页面
    #     self.login_page.submit_userinfo(data['phone'], data['password'])
    #     # 断言
    #     self.assertTrue(data['expected'] == self.login_page.alert_info().text)

    # def test_bid_send1_wrong(self):

    def test_bid_0_success(self):
        # 首页点击投标
        IndexPage(self.driver).bid()
        # 输入投标金额
        self.bid_page.send_bid(bid_data.bid_correct['money'])
        # 点击投标
        self.bid_page.submit_bid()

        # 断言1.弹出框有投标成功！
        self.assertTrue(self.bid_page.bid_success_popup.text == bid_data.bid_correct['expected'])
        # 断言2.比对余额
        # 断言3.投资记录


if __name__ == "__main__":
    unittest.main()


