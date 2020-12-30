#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: 3test_demo_03.py
# @time: 2020/12/30 8:36 下午

import pytest

@pytest.fixture(params=[(1,1,2),(3,9,12),(7,18,25)],ids=['add01','add02','add03'])
def setUp(request):
    return request.param

class TestDemo03:
    def testadd(self, setUp):
        print('exec TestDemo03 --> testadd')
        assert setUp[0]+setUp[1] == setUp[2]