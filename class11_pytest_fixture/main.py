# -*- coding: utf-8 -*-
# @Time     : 2020/3/24 17:14
# @Author   : Zhou_Chao
# @Email    : 1031529989@qq.com
# @File     : main.py
# @Software : 
import pytest

if __name__ == '__main__':
    pytest.main(['-m all',
                 '--capture=no'
                 ])

    # pytest.main(['-m all',
    #              '--result-log=reports/test.txt',
    #              '--junit-xml=reports/test.xml',
    #              '--html=reports/test.html'])


    # allure版测试报告
    # allure-commandline-2.1.0.0.zip

