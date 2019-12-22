"""
Time:2019/12/18 0018
"""
import unittest
import os
import time

from HTMLTestRunnerNew import HTMLTestRunner
from scripts.handle_path import PATH_CASES, REPORT_PATH
from scripts.handle_config import hy

class RunTest:
    def run_cases(self):
        suit = unittest.defaultTestLoader.discover(PATH_CASES)
        time_str = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        runner = HTMLTestRunner(stream=open(os.path.join(REPORT_PATH, f'reporter{time_str}.html'), 'wb'),
                                description='这是我的测试报告',
                                tester='y.h',
                                title='测试报告')
        runner.run(suit)


if __name__ == '__main__':
    rt = RunTest()
    rt.run_cases()
