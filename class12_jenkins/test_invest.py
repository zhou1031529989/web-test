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

from class12_jenkins.datas import login_data, bid_data
from class12_jenkins.pages.bid_page import BidPage
from class12_jenkins.pages.index_page import IndexPage
from class12_jenkins.pages.login_page import LoginPage


class TestInvest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get('http://120.78.128.25:8765/Index/login.html')
        cls.driver.maximize_window()
        cls.login_page = LoginPage(cls.driver)
        cls.login_page.submit_userinfo(
            login_data.user_correct['phone'], login_data.user_correct['password'])
        cls.bid_page = BidPage(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


    def setUp(self):
        print("*****************开始执行测试用例*******************")

    def tearDown(self):
        self.driver.refresh()

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

        # 点击×
        self.bid_page.x_()

    def test_bid_send10_popup(self):
        # 输入投标金额
        self.bid_page.send_bid(bid_data.bid_uncorrect['money'])
        # 点击投标
        self.bid_page.submit_bid()
        # 断言1.弹出框提示有！
        self.assertTrue(self.bid_page.bid_failed_popup.text == bid_data.bid_uncorrect['expected'])
        # 断言2.比对余额
        # 点击确认
        self.bid_page.confirm_()

    def test_bid_send1_wrong(self):
        # 输入投标金额
        self.bid_page.send_bid(bid_data.bid_uncorrect2['money'])
        # 断言1.投标按钮变成请输入10的整数倍
        self.assertTrue(self.bid_page.bid_failed2_popup.text == bid_data.bid_uncorrect2['expected'])
        # 断言2.比对余额


if __name__ == "__main__":
    unittest.main()


