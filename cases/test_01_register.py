"""
Time:2019/12/22 0022
"""

import unittest

from libs.ddt import ddt, data
from scripts.handle_excel import HandleExcel
from scripts.handle_config import hy
from scripts.handle_re import HandleRe
from scripts.handle_mysql import HandleMysql
from scripts.handle_request import HandleRequest
from scripts.handle_log import mylogger


@ddt
class TestRegister(unittest.TestCase):
    he = HandleExcel('register')
    obj_li = he.read_excel()
    hm = HandleMysql()
    hr = HandleRequest()

    @classmethod
    def setUpClass(cls):
        cls.hr.common_head({
            "X-Lemonban-Media-Type": "lemonban.v2"
        })

    @data(*obj_li)
    def test_register(self, obj):
        register_url = hy.read_yaml('mysql', 'url') + obj.url
        phone_num = self.hm.get_noexist_phone(hy.read_yaml('mysql', 'sql'))
        json_data = HandleRe.use_re(phone_num, obj.data)
        res = self.hr.send(url=register_url, data=json_data)
        try:
            self.assertEqual([obj.expected, obj.msg], [res.json()['code'], res.json()['msg']], msg=f'{obj.title}执行完毕')
        except AssertionError as a:
            self.he.write_excel(obj.caseId + 1, 7, 'fail')
            mylogger.error(a)
            raise a
        else:
            self.he.write_excel(obj.caseId + 1, 7, 'success')
            mylogger.info(obj.title)
        finally:
            self.he.write_excel(obj.caseId + 1, 8, str(res.json()))

    @classmethod
    def tearDownClass(cls):
        cls.hm.close()
        cls.hr.close()
