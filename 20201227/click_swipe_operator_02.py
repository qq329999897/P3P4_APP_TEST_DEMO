#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: click_swipe_operator_02.py
# @time: 2020/12/27 9:08 上午

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
# driver.tap([(216,1511),(216,1943),(216,2375)],1000)
# element1 = driver.find_element_by_xpath('//android.widget.TextView[@text="存储"]')
# element2 = driver.find_element_by_xpath('//android.widget.TextView[@text="应用和通知"]')
# driver.scroll(element1,element2,2000)
# driver.drag_and_drop(element1,element2)
# driver.flick( 216,2375,216,1511 )
# driver.swipe( 216,2375,216,1511,3000)
# 使用坐标进行滑动，如果要操作多台手机的话，由于手机分辨率不一样，导致滑动不准确
# 一般情况下，1 使用scroll、drag_and_drop进行滑动操作 2 获取屏幕分辨率、进行比例换算
size = driver.get_window_size() # {'width':..,'height':...} 1440  2816
print( size )
# driver.swipe(size['width']/2,size['height']*3/4,size['width']/2,size['height']/4,3000)

# driver.tap([(216,2375)],1000)

# print( 216/size['width'],2375/size['height'] )  #  安全性与位置信息 在屏幕的%位置  0.15  0.84
print( int(size['width']*0.15),int(size['height']*0.84) )
driver.tap([ (int(size['width']*0.15),int(size['height']*0.84)) ],1000)

# 思路：
# 1、查找元素 或者元素的 bounds 比如 [216,2375][600,2440]
# 2、为了之后能稳定的点击该元素 ，先取元素正中间的点 [ 816/2 , 4815/2]
# 3、把得到的元素正中间的点的坐标和屏幕分辨率进行除法  816/2/1440  4815/2/2816
# 4、获取当前手机的屏幕分辨率，int(size['width'] * x坐标除法结果),int(size['height'] * y坐标除法结果)
