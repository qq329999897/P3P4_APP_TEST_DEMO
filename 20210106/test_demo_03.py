#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: 1test_demo_01.py
# @time: 2021/1/6 8:22 下午

import pytest
import allure

# pytestmark=pytest.mark.skip()

@allure.epic('计算器系统V1.0')
@allure.feature('加法模块')
class TestDemo03:
    @pytest.mark.skip(reason="无条件跳过")
    def test_add_01(self):
        print( 'exec TestDemo02 test_add_01' )
        assert 1+1 == 2
    # @pytest.mark.skipif(10,reason="条件为真时跳过")  # True  非0 非空  1>0
    def test_add_02(self):
        print( 'exec TestDemo02 test_add_02' )
        assert 1+1 == 2

    def test_add_03(self):
        # if True:
        #     pytest.skip('方法内部直接跳过')
        print( 'exec TestDemo02 test_add_03' )
        assert 1+1 == 2