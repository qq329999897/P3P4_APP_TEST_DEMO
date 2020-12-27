#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: test1_fixtrue_03.py
# @time: 2020/12/27 5:10 下午

import pytest

@pytest.fixture(scope='module')
def sss():
    print('测试初始化')
    yield
    print('测试环境清理')

def test_case_01(sss):
    print('执行test_case_01')
    assert True

def test_case_02(sss):
    print('执行test_case_02')
    assert True

if __name__=='__main__':
    pytest.main(["-s"])  # -s 显示print信息