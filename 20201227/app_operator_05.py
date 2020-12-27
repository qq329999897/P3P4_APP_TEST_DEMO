#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: app_operator_05.py
# @time: 2020/12/27 11:33 上午

import time
import os
from appium import webdriver
from appium.webdriver.connectiontype import ConnectionType

# 配置项
des = {
    "platformName":"android",
    "platformVersion":"8.0",
    "deviceName":"Samsung Galaxy S8",
    "udid":"192.168.56.101:5555",
    "appPackage":"com.ibox.calculators",
    "appActivity":".CalculatorActivity",
    "noReset":True,
    "unicodeKeyboard": True,
    "resetKeyboard": True,
    "newCommandTimeout":30
}
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",des)
# if driver.is_app_installed('com.ibox.calculators'):
#     driver.remove_app('com.ibox.calculators')
#     time.sleep(3)
# driver.install_app( os.path.join(os.path.dirname(__file__),'jisuanqi_587.apk') )
# time.sleep(3)
# driver.start_activity( 'com.ibox.calculators','.CalculatorActivity' )
# driver.background_app(5)
# time.sleep(2)
# driver.close_app()
# time.sleep(2)
# driver.launch_app()
# time.sleep(2)
# driver.start_activity( 'com.ibox.calculators','.CalculatorActivity' )
time.sleep(5)
driver.find_element_by_xpath('//android.widget.Button[@resource-id="com.ibox.calculators:id/update_id_cancel"]').click()
time.sleep(2)
driver.activate_app('com.android.settings')
