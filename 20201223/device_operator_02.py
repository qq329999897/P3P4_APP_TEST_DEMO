#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: device_operator_02.py
# @time: 2020/12/23 8:46 下午

import time
from appium import webdriver
from appium.webdriver.connectiontype import ConnectionType

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

# driver.lock()
# time.sleep(2)
# if driver.is_locked():  # 判断是否锁屏  锁屏：true
#     driver.unlock()

# driver.open_notifications()  # 打开通知栏

# print( driver.orientation ) # 显示横竖屏情况
# driver.orientation = 'LANDSCAPE' #切换成横屏
# time.sleep(3)
# driver.orientation = 'PORTRAIT'  #切换成竖屏

# print( driver.get_window_size() ) # 获取手机屏幕尺寸

# print( driver.network_connection ) # 获取目前的网络状态
#
# driver.set_network_connection(1) # 设置成飞行模式
# time.sleep(3)
# print( driver.network_connection )
# driver.set_network_connection( ConnectionType.ALL_NETWORK_ON ) # 设置网络全开模式
# time.sleep(2)
# print( driver.network_connection )

# driver.save_screenshot("./test1.png")

print( driver.get_device_time() )