# -*- coding: utf-8 -*-
# @Time     : 2020/3/19 22:53
# @Author   : Zhou_Chao
# @Email    : 1031529989@qq.com
# @File     : d1.py
# @Software :

# web测试的内容
"""
api.github.com/?sff

接口测试只测试数据（后台返回的结果符合要求否），web测试测试UI交互效果、链接跳转、浏览器兼容性和数据等

接口测试全部通过后，web测试出现的问题就是前端的问题

"""
# python  与 浏览器关系
"""
python  通过[接口]  访问[后端服务]

接口 USB 耳机接口，interface  [接口是做适配用的]

UI  》》》 user interface(用户界面接口)

API 》》》application programming interface(应用程序编程接口)

函数 python Java 私有方法，公有方法（就是接口） private protected
"""

# python  怎么访问浏览器

"""
python 通过[webdriver] 访问 浏览器

接口 selenium，或自己写一个接口

"""

# web自动化环境安装
"""
1.安装selenium
命令行使用以下命令安装selenium：
pip install -U selenium

（pip install --help 查-U的意思）

2.安装Chrome浏览器Chrome和Chromedriver
下载链接：https://pan.baidu.com/s/1eSct8LO 密码：xeca

3.Chromedriver放在python的安装根目录下面即可。
下载链接中，只提供了Windows版本的Chrome和Chromedriver。
其他操作系统需要另外下载。
Chromedriver下载地址：
http://npm.taobao.org/mirrors/chromedriver/
查看Chrome的版本，打开浏览器-设置-关于Chrome（版本要与下载的Chromedriver一致）

"""

from selenium import webdriver

driver = webdriver.Chrome()     # 浏览器对象

















