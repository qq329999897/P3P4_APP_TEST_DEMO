#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: test_demo_06_01.py
# @time: 2020/12/30 9:19 下午

# pytest默认执行顺序：包/文件-->根据ascii码升序执行,文件内部的测试方法-->哪个方法写在前面就优先执行
import pytest

class TestDemo0602:
    @pytest.mark.run(order=1)
    def testadd03(self):
        print('exec TestDemo0602 --> testadd03')
        assert 1+1==2
    @pytest.mark.run(order=2)
    def testadd04(self):
        print('exec TestDemo0602 --> testadd04')
        assert 1+1==2
    @pytest.mark.run(order=3)
    def testadd01(self):
        print('exec TestDemo0602 --> testadd01')
        assert 1+1==2
    @pytest.mark.run(order=4)
    def testadd02(self):
        print('exec TestDemo0602 --> testadd02')
        assert 1+1==2
