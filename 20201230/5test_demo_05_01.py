#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: 5test_demo_05_01.py
# @time: 2020/12/30 9:04 下午

import pytest

class TestDemo0501:
    @pytest.mark.smoketest
    @pytest.mark.systemtest
    def test_add_01(self):
        print( 'exec TestDemo0501-->test_add_01' )
        assert 1+3==4

    @pytest.mark.systemtest
    def test_add_02(self):
        print( 'exec TestDemo0501-->test_add_02' )
        assert 1+3==4