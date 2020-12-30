#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: conftest.py
# @time: 2020/12/30 8:50 下午

import pytest

@pytest.fixture(name='test_package_02')
def setUp():
    print('test_package_02 开始运行初始化')
    yield
    print('test_package_02 结束运行自动化')