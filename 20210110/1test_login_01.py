#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: 1test_login_01.py
# @time: 2021/1/10 9:01 上午

import pytest
import allure

@allure.epic('[epic]NEWDREAM_学生管理系统')
@allure.feature('[feature]NEWDREAM_学生管理系统V1.0')
class TestLogin01:
    @allure.story('[story]登录模块')
    @allure.title('[title]case01 验证正确的用户名和密码能否成功登录')
    def test_login_success(self):
        assert True

    @allure.story('[story]登录模块')
    @allure.title('[title]case02 验证错误的用户名和密码能否成功登录')
    def test_login_fail(self):
        assert True

