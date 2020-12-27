#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: touch_action_operator_04.py
# @time: 2020/12/27 10:45 上午

import time
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

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
# element01 = driver.find_element_by_xpath('//android.widget.TextView[@text="电池"]')
# TouchAction(driver).press(element01).release().perform()  # 点击操作
# long_press bug ：放入元素操作的时候，会把元素的bounds属性 相加/2 得出x,y坐标 ，计算出现小数会导致坐标判断失败
# （因为坐标必须是整型）
# TouchAction(driver).long_press(None,216,1511,5000).perform()  # 长按操作 bug

element1 = driver.find_element_by_xpath('//android.widget.TextView[@text="设置屏幕锁定"]')
touch_action = TouchAction(driver)
touch_action.press(element1).release().perform()
time.sleep(2)
element2 = driver.find_element_by_xpath('//android.widget.TextView[@text="图案"]')
touch_action.press(element2).release().perform()
time.sleep(2)
# 287,1329  287,1762  725,1762  725,2196  1154,1762   725,1329
touch_action.press(x=287,y=1329).wait(1000)\
                    .move_to(x=287,y=1762).wait(1000)\
                    .move_to(x=725,y=1762).wait(1000)\
                    .move_to(x=725,y=2196).wait(1000)\
                    .move_to(x=1154,y=1762).wait(1000)\
                    .move_to(x=725,y=1329).wait(1000)\
                    .release().perform()
