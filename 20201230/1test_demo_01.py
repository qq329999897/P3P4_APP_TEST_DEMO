#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: 1test_demo_01.py
# @time: 2020/12/30 8:14 下午

import pytest

@pytest.fixture(autouse=True)
def setUp():
    print( '测试初始化' )
    yield
    print( '测试环境清理')

class TestDemo01:
    def testadd(self):
        print( 'exec TestDemo01 -- > testadd' )
        assert 1+1 == 2
    def testsub(self):
        print( 'exec TestDemo01 -- > testsub' )
        assert 1-1 == 0