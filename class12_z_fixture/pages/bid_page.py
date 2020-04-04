# -*- coding: utf-8 -*-
# @Time     : 2020/3/23 22:34
# @Author   : Zhou_Chao
# @Email    : 1031529989@qq.com
# @File     : bid_page.py
# @Software :
from selenium.webdriver.common.by import By

from class12_z_fixture.pages.base import BasePage




class BidPage(BasePage):
    # 可用余额定位器
    bid_input_locator = (By.XPATH,"//input[contains(@class,'invest-unit-investinput')]")

    # 投标定位器
    bid_submit_locator = (By.XPATH, "//button[contains(@class,'height_style')]")

    # 投标成功弹框定位器
    bid_success_popup_locator = (By.XPATH, "//div[@class='layui-layer-content']//div[contains(@class, 'capital_font1')]")

    # 叉掉成功弹框定位器
    x = (By.XPATH, "//div[@class='layui-layer-content']//div[@class='close_pop']/img")

    # 投资不为100倍数提示定位器
    message = (By.XPATH, "//div[text()='投标金额必须为100的倍数']")

    # 投资不为100整数倍，提示确认定位器
    confirm = (By.XPATH, '//a[text() = "确认"]')

    # 投资不为10整数倍定位器
    money = (By.XPATH, '//button[text()="请输入10的整数倍"]')


    # 1.找到投资框
    @property
    def bid_input_element(self):
        print("bid element")
        return self.get_clickable_element(self.bid_input_locator)
    # 输入投资金额
    def send_bid(self, money):
        return self.bid_input_element.send_keys(money)

    # 2.找到投标按钮
    @property
    def bid_submit_element(self):
        return self.get_visible_element(self.bid_submit_locator)
    # 点击投标
    def submit_bid(self):
        return self.bid_submit_element.click()

    # 3.找到投资成功提示框,以text内容进行断言
    @property
    def bid_success_popup(self):
        return self.get_visible_element(self.bid_success_popup_locator)

    # 4.?
    # @property
    # def submit_text(self):
    #     return self.bid_submit_element.text

    # 4.找到成功弹框x，叉掉成功弹框
    @property
    def x_element(self):
        return self.get_visible_element(self.x)
    # 点击X
    def x_(self):
        return self.x_element.click()

    # 5.找到提示框,以text内容进行断言（投资10元）
    @property
    def bid_failed_popup(self):
        return self.get_visible_element(self.message)

    # 6.找到提示框
    @property
    def  prompt_element(self):
        return self.get_clickable_element(self.confirm)
    # 点击确认
    def confirm_(self):
        return self.prompt_element.click()


    # 7.找到投标按钮变灰，返回文本内容进行断言
    @property
    def bid_failed2_popup(self):
        return self.get_visible_element(self.money)


