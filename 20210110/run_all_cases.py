#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: run_all_cases.py
# @time: 2021/1/10 9:01 上午

import os
import time
import pytest


current_path = os.path.dirname(__file__)
json_report_path = os.path.join( current_path ,'json_report' )
html_report_path = os.path.join(  current_path,'html_report',time.strftime('%Y%m%d_%H%M%S'))

# pytest.main(['-s','-v','--alluredir=%s'%json_report_path,'--clean-alluredir'])
pytest.main(['-s','-v','--allure-stories=%s'%'[story]学生新增,[story]学生修改','--alluredir=%s'%json_report_path,'--clean-alluredir'])
# pytest.main(['-s','-v','--allure-severities=blocker,critical','--alluredir=%s'%json_report_path,'--clean-alluredir'])

os.system('allure generate %s -o %s --clean'%(json_report_path,html_report_path))