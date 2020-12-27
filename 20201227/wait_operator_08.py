#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: wait_operator_08.py
# @time: 2020/12/27 4:45 下午

import time
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

# 配置项
des = {
    "platformName":"android",
    "platformVersion":"8.0",
    "deviceName":"Samsung Galaxy S8",
    "appPackage":"com.android.settings",
    "appActivity":".Settings",
    "udid":"192.168.56.101:5555",
    "noReset":True,
    "unicodeKeyboard": True,
    "resetKeyboard": True,
    "newCommandTimeout":30
}
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",des)
# time.sleep(3)
# driver.implicitly_wait(20)  全局设置、每隔500ms在页面上检查一次

element1 = WebDriverWait(driver,10).until(lambda x:x.find_element_by_xpath('//android.widget.TextView[@text="存储"]'))

element1.click()
