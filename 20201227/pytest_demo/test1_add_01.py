#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: test1_add_01.py
# @time: 2020/12/27 5:00 下午

import pytest

class Testadd01:
    def test_add_case_01(self):
        assert 1+1 == 2

if __name__=='__main__':
    pytest.main()
