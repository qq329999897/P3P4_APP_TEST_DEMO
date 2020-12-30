#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: conftest.py
# @time: 2020/12/30 8:50 下午

import pytest

@pytest.fixture(name='main_package')
def setUp():
    print('main_package 开始运行初始化')
    yield
    print('main_package 结束运行自动化')