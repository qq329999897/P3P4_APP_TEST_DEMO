#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: 1test_login_01.py
# @time: 2021/1/10 9:01 上午

import pytest
import allure

@allure.epic('[epic]NEWDREAM_学生管理系统')
@allure.feature('[feature]NEWDREAM_学生管理系统V1.0')
class TestStuManage02:
    @allure.story('[story]学生新增')
    @allure.title('[title]case01 验证能否成功添加学生信息')
    def test_add_stu_info(self):
        assert True

    @allure.story('[story]学生修改')
    @allure.title('[title]case02 验证能否成功修改学生信息')
    @allure.severity(allure.severity_level.BLOCKER)
    def test_update_stu_info(self):
        assert True

