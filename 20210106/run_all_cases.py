#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: run_all_cases.py
# @time: 2021/1/6 8:22 下午

import pytest
import os

# pytest.main(['-s','-v','-m smoketest or test_demo_01'])
# pytest.main(['-s','-v','-m smoketest and test_demo_01'])
# pytest.main(['-s','-v','-m not smoketest'])

pytest.main(['--alluredir=./allure_report','--clean-alluredir'])
os.system( 'allure generate ./allure_report -o ./allure_html_report --clean' )
