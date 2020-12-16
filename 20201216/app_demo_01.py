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
    "appPackage":"com.android.calculator2",
    "appActivity":".Calculator",
    "udid":"192.168.56.101:5555",
    "noReset":True,
    "unicodeKeyboard": True,
    "resetKeyboard": True,
    "newCommandTimeout":30
}
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",des)
# 根据text定位
# driver.find_element_by_android_uiautomator('new UiSelector().text("9")').click()
# driver.find_element_by_android_uiautomator('text("9")').click()
# driver.find_element_by_android_uiautomator('new UiSelector().textStartsWith("8")').click()
# driver.find_element_by_android_uiautomator('new UiSelector().textContains("6")').click()

# driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.android.calculator2:id/digit_6")').click()
# driver.find_element_by_android_uiautomator('new UiSelector().description("加")').click()
# driver.find_element_by_android_uiautomator('new UiSelector().className("android.widget.Button").text("9")').click()

# driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.android.calculator2:id/pad_numeric").childSelector(className("android.widget.Button").instance(3))').click()
driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.android.calculator2:id/digit_4").fromParent(text("9"))').click()



