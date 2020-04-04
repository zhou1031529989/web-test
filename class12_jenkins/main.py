# -*- coding: utf-8 -*-
# @Time     : 2020/3/24 17:14
# @Author   : Zhou_Chao
# @Email    : 1031529989@qq.com
# @File     : main.py
# @Software : 
import pytest
import os

xml_report_path = "./reports/xml"
html_report_path = "./reports/html"

if __name__ == '__main__':

    pytest.main(['-m all',
                 '--capture=no',
                 '--alluredir=allure'
                 ])


    # pytest.main(['-m all',
    #              '--result-log=reports/test.txt',
    #              '--junit-xml=reports/test.xml',
    #              '--html=reports/test.html'])


    # allure版测试报告
    # allure-commandline-2.1.0.0.zip

    # 分布式
    # master - slaves
    """
    
    1.配置Jenkins：
    系统管理-节点管理（给服务器添加一个节点）-New Node-Node name-OK
    Configure-Launch method(通过Java Web启动代理)-工具位置（NAME:(Allure Commandline)allure210）(Home:F:\allure\allure-commandline-2.13.2\allure-2.13.2)
    2.连接主人：
    Python13 - Launch （第一个如果失败，用命令行在相应的盘运行复制的第二行内容）
    3.分配任务：
    New任务-Configure-General(Restrict where this project can be run)放到刚才建的节点python13上面去跑 - 源码管理Git - Build (如果选择无，通过本地运行)
    - Command (C:\\Users\zhouchao\PycharmProjects\python13-web\class12_jenkins python main.py)
    (如果不在C盘
    d:
    cd D:\jenkins_10_slave\class10_pytest
    python main.py) 如果复制到Jenkins的工作目录里面，就不需要cd切换了 直接 python main.py
    - Post-build-Actions  -Results  -Path (allure)
    4.生成allure测试报告
    系统管理-插件管理-Allure-如果没有找到到Jenkins查检中心搜索地址，搜索allure下载，然后将文件上传到Upload Plugin
    -全局工具配置-Allure Commandline -Add Allure Commandline -(Name:allure2132)(Installation directory:F:\allure\allure-commandline-2.13.2\allure-2.13.2)
    -勾选自动安装
    
    """
