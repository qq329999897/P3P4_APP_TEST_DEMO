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
    "appPackage":"com.android.contacts",
    "appActivity":".activities.PeopleActivity",
    "udid":"192.168.56.101:5555",
    "noReset":True,
    "unicodeKeyboard": True,
    "resetKeyboard": True,
    "newCommandTimeout":30
}
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",des)

time.sleep(1)
driver.tap( [(1307,2690)],1000 )
