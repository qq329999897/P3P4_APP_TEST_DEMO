#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: h5_demo_02.py
# @time: 2020/12/16 9:07 下午

from appium import webdriver
import time
# 配置项
des = {
    "platformName":"android",
    "platformVersion":"8.0",
    "deviceName":"Samsung Galaxy S8",
    "udid":"192.168.56.101:5555",
    "browserName":"chrome", # 打开浏览器类型
    "noReset":True,
    "unicodeKeyboard": True,
    "resetKeyboard": True,
    "newCommandTimeout":30,
    "chromedriverExecutable":"/Users/liuqingjun/Desktop/chromedriver" # 指定chromedriver路径
}
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",des)
driver.get('https://www.qq.com')
driver.implicitly_wait(10)

# H5网页的识别方式和之前学习selenium的一致
# driver.find_element_by_link_text('体育').click()
driver.find_element_by_xpath('//a[@href="/m/sports"]').click()
time.sleep(2)
driver.back()
time.sleep(2)
driver.forward()
time.sleep(2)
driver.refresh()
time.sleep(1)
title = driver.title
print( title )
url = driver.current_url
print( url )
driver.quit()