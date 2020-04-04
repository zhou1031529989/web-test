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
import pytest

from class12_z_fixture.datas import bid_data

from class12_z_fixture.pages.index_page import IndexPage

@pytest.mark.all_
@pytest.mark.usefixtures('my_set2_class')
class TestInvest():

    @pytest.mark.smoke
    def test_bid_0_success(self,my_set2_class):
        driver, bid_page = my_set2_class
        # 首页点击投标
        IndexPage(driver).bid()
        # 输入投标金额
        bid_page.send_bid(bid_data.bid_correct['money'])
        # 点击投标
        bid_page.submit_bid()

        # 断言1.弹出框有投标成功！
        assert(bid_page.bid_success_popup.text == bid_data.bid_correct['expected'])
        # 断言2.比对余额
        # 断言3.投资记录

        # 点击×
        bid_page.x_()

        driver.refresh()

    def test_bid_send10_popup(self,my_set2_class):
        driver, bid_page = my_set2_class
        # 输入投标金额
        bid_page.send_bid(bid_data.bid_uncorrect['money'])
        # 点击投标
        bid_page.submit_bid()
        # 断言1.弹出框提示有！
        assert(bid_page.bid_failed_popup.text == bid_data.bid_uncorrect['expected'])
        # 断言2.比对余额
        # 点击确认
        bid_page.confirm_()

        driver.refresh()

    def test_bid_send1_wrong(self,my_set2_class):
        driver, bid_page = my_set2_class
        # 输入投标金额
        bid_page.send_bid(bid_data.bid_uncorrect2['money'])
        # 断言1.投标按钮变成请输入10的整数倍
        assert(bid_page.bid_failed2_popup.text == bid_data.bid_uncorrect2['expected'])
        # 断言2.比对余额


if __name__ == "__main__":
    unittest.main()


