#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: webview_operator_06.py
# @time: 2020/12/27 2:19 下午

import time
import os
from appium import webdriver

des = {
    "platformName":"android",
    "platformVersion":"8.0",
    "deviceName":"Samsung Galaxy S8",
    "udid":"192.168.56.101:5555",
    "browserName":"chrome", # 打开浏览器类型
    "noReset":True,
    "unicodeKeyboard": True,
    "resetKeyboard": True,
    "newCommandTimeout":30
}
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",des)
driver.get('https://www.baidu.com')
time.sleep(5)
print( driver.current_context )
print( driver.context )
print( driver.contexts )
driver.switch_to.context('NATIVE_APP')  # 切换到原生的app
driver.find_element_by_xpath('//android.widget.Button[@resource-id="com.android.chrome:id/positive_button"]').click()
time.sleep(5)
driver.find_element_by_xpath('//android.widget.Button[@resource-id="com.android.packageinstaller:id/permission_allow_button"]').click()
time.sleep(2)
driver.switch_to.context('CHROMIUM')  # 切换回CHROMIUM
time.sleep(2)
driver.find_element_by_xpath('//input[@id="index-kw"]').send_keys('newdream') # id方法等不能正常使用
time.sleep(2)
driver.find_element_by_xpath('//button[@id="index-bn"]').click()
