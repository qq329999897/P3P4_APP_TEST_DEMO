#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: key_operator_01.py
# @time: 2020/12/27 8:47 上午

import time
from appium import webdriver
from appium.webdriver.connectiontype import ConnectionType

# 配置项
des = {
    "platformName":"android",
    "platformVersion":"8.0",
    "deviceName":"Samsung Galaxy S8",
    "appPackage":"com.android.dialer",
    "appActivity":".app.DialtactsActivity",
    "udid":"192.168.56.101:5555",
    "noReset":True,
    "unicodeKeyboard": True,
    "resetKeyboard": True,
    "newCommandTimeout":30
}
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",des)

driver.find_element_by_xpath('//android.widget.FrameLayout[@bounds="[0,72][1440,264]"]').click()
time.sleep(1)
driver.find_element_by_id('com.android.dialer:id/search_view').click()
time.sleep(1)
# driver.keyevent(29,1048576)
driver.long_press_keycode(24)