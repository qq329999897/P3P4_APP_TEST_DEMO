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
    "appPackage":"com.wondertek.paper",
    "appActivity":"cn.thepaper.paper.ui.main.MainActivity",
    "noReset":True,
    "unicodeKeyboard": True,
    "resetKeyboard": True,
    "newCommandTimeout":30
}
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",des)
time.sleep(10)
print( driver.current_context )
print( driver.contexts)
driver.find_element_by_xpath('//android.widget.TextView[@text="阵痛下的成长：以新规范新姿态拥抱未来"]').click()
time.sleep(10)
# print( driver.contexts)
# driver.find_element_by_xpath('//android.widget.ImageView[@resource-id="com.wondertek.paper:id/post_praise_img"]').click()
# time.sleep(2)
# print( driver.contexts)
driver.switch_to.context('WEBVIEW_com.wondertek.paper')
time.sleep(5)
value = driver.find_element_by_xpath('//section[2]/div/div/b[1]').text
print( value )
# driver.find_element_by_xpath('//android.widget.TextView[@resource-id="com.wondertek.paper:id/title"]').click()
# time.sleep(2)
# print( driver.contexts)
# driver.find_element_by_xpath('//android.widget.Button[@resource-id="com.wondertek.paper:id/one_key_confirm"]').click()
# time.sleep(2)
# print( driver.contexts)
