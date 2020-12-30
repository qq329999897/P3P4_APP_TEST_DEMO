#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: 2test_demo_02.py
# @time: 2020/12/30 8:23 下午

import pytest

@pytest.fixture(params=[1, 2, 3, 4, 5], ids=['num1', 'num2', 'num3', 'num4', 'num5'])
def setUp(request):
    return request.param


class TestDemo02:
    def testadd(self, setUp):
        print('exec TestDemo02 --> testadd')
        assert 2 >= setUp
