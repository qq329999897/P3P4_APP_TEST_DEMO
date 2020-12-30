#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: 1test_demo_01.py
# @time: 2020/12/30 8:14 下午

class TestDemo01:
    def testadd(self,main_package,test_package_01):
        print( 'exec TestDemo01 -- > testadd' )
        assert 1+1 == 2
    def testsub(self):
        print( 'exec TestDemo01 -- > testsub' )
        assert 1-1 == 0