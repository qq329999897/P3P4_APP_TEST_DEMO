#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: 1test_login_01.py
# @time: 2021/1/10 9:01 上午

import os
import pytest
import allure

@pytest.fixture(name='set')
def set_up():
    print('前置条件：***')
    yield
    print('后置处理：***')

@allure.step('步骤一：调用首页接口获取token')
def step_01():
    pass
@allure.step('步骤二：调用登录接口')
def step_02():
    pass
@allure.epic('[epic]NEWDREAM_学生管理系统')
@allure.feature('[feature]NEWDREAM_学生管理系统V1.0')
class TestLogin03:
    @allure.story('[story]登录模块')
    @allure.title('[title]case01 验证正确的用户名和密码能否成功登录')
    @allure.testcase('http://47.107.178.45/zentao/www/index.php?m=testcase&f=view&caseID=10&version=1',name='用例链接')
    @allure.issue('http://47.107.178.45/zentao/www/index.php?m=bug&f=browse&productID=4',name='缺陷地址')
    @allure.link(url='http://www.hnxmxit.com',name='公司官网')
    @allure.description('登录测试用例 作者：小红 时间：20210110')
    # @allure.severity('blocker')
    @allure.severity(allure.severity_level.BLOCKER)
    def test_login_success(self,set):
        step_01()
        step_02()
        with allure.step('步骤三：验证判断'):
            pass
        with allure.step('步骤四：验证判断'):
            pass
        with open(os.path.join(os.path.dirname(__file__),'imgs','screenshot.jpeg'),'rb') as img_file:
            img_obj = img_file.read()
            allure.attach(img_obj,'用例执行出错截图',allure.attachment_type.JPG)
        assert True

    @allure.story('[story]登录模块')
    @allure.title('[title]case02 验证错误的用户名和密码能否成功登录')
    @allure.severity('critical')
    def test_login_fail(self,set):
        assert True

