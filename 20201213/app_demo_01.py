#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: app_demo_01.py
# @time: 2020/12/13 2:26 下午

from appium import webdriver
# 配置项
des = {
    "platformName":"android",
    "platformVersion":"8.0",
    "deviceName":"Samsung Galaxy S8",
    # "app":"/Users/liuqingjun/Desktop/app/jisuanqi_587.apk",
    "appPackage":"com.android.calculator2",
    "appActivity":".Calculator",
    "udid":"192.168.56.101:5555",
    "noReset":True,
    "unicodeKeyboard": True,
    "resetKeyboard": True,
    "newCommandTimeout":30
}
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",des)
# driver.find_element_by_id("com.android.calculator2:id/digit_9").click()
# driver.find_element_by_id("com.android.calculator2:id/op_add").click()
# driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.view.ViewGroup[1]/android.widget.Button[3]").click()
# driver.find_element_by_xpath('//android.widget.Button[@text="9"]').click()
driver.find_element_by_xpath('//android.widget.Button[@bounds="[612,1548][894,1859]" and @text="9"]').click()
# driver.find_element_by_accessibility_id('加').click()  # content-desc
driver.find_element_by_xpath('//android.widget.Button[ends-with(@resource-id,"op_add")]').click()
driver.find_element_by_id("com.android.calculator2:id/digit_7").click()
driver.find_element_by_id("com.android.calculator2:id/eq").click()
# driver.find_element_by_name()
