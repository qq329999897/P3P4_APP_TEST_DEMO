#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: 1test_demo_01.py
# @time: 2021/1/6 8:22 下午

import pytest

class TestDemo01:
    @pytest.mark.smoketest
    @pytest.mark.test_demo_01
    def test_add_01(self):
        print( 'exec TestDemo01 test_add_01' )
        assert 1+1 == 2
    @pytest.mark.test_demo_01
    def test_add_02(self):
        print( 'exec TestDemo01 test_add_02' )
        assert 1+1 == 2
    @pytest.mark.test_demo_01
    def test_add_03(self):
        print( 'exec TestDemo01 test_add_03' )
        assert 1+1 == 2