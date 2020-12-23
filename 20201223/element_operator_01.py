#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: element_operator_01.py
# @time: 2020/12/23 8:26 下午

from appium import webdriver
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
app_element = driver.find_element_by_xpath('//android.widget.TextView[ends-with(@text,"正在充电")]')

# print( app_element.text )
# print( app_element.tag_name )
# print( app_element.get_attribute("bounds") )
# print( app_element.size )
# print( app_element.location )
# print( app_element.rect )
# app_element.screenshot('./test.png')
print( app_element.get_attribute("displayed") )
print( app_element.is_enabled() )
print( app_element.is_selected() )
print( app_element.is_displayed() )
