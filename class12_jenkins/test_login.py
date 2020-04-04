# -*- coding: utf-8 -*-
# @Time     : 2020/3/23 13:06
# @Author   : Zhou_Chao
# @Email    : 1031529989@qq.com
# @File     : 163.py
# @Software :

import unittest

import pytest

from class12_jenkins.datas import login_data
from class12_jenkins.pages.index_page import IndexPage


# 1.测试类要以Test开头
# 2.测试模块要你test_开头或_test结尾
# 3.测试类里面不能有__init__方法
# 4.测试方法要以test开头

# 有了conftest文件后，测试类不要再继承unittest.TestCase了
# 设置类环境
@pytest.mark.usefixtures('my_set_class')
@pytest.mark.all
class TestLogin():

    @pytest.mark.smoke
    @pytest.mark.parametrize("data", login_data.user_incorrect)
    def test_login_1_failed(self,data,my_set_class):
        # yield 返回需要用的driver，和login_page
        driver, login_page = my_set_class
        # 访问登录页面
        login_page.submit_userinfo(data['phone'], data['password'])
        # 断言
        assert(data['expected'] == login_page.alert_info().text)
        login_page.clear_phone()
        login_page.clear_pwd()


    @pytest.mark.login
    @pytest.mark.parametrize("data", login_data.user_unauthorized)
    def test_login_0_failed(self,data,my_set_class):
        driver, login_page = my_set_class
        # 访问登录页面
        login_page.submit_userinfo(data['phone'], data['password'])
        print(data['expected'])
        print(login_page.unauthorized_info().text)
        # 断言
        assert(data['expected'] == login_page.unauthorized_info().text)
        login_page.clear_phone()
        login_page.clear_pwd()

    def test_login_2_success(self,my_set_class):
        driver, login_page = my_set_class
        login_page.submit_userinfo('18684720553','python')
        user_ele = IndexPage(driver).get_user()
        assert('华华' in user_ele.text)

if __name__ == "__main__":
    unittest.main()















