"""
Time:2019/12/22 0022
"""
import os

from scripts.handle_mysql import HandleMysql
from scripts.handle_path import PHONE_CONF
from scripts.handle_request import HandleRequest
from scripts.handle_config import hy, HandleYaml


class HandlePhone:
    def __init__(self, filepath=None):
        if filepath:
            self.filepath = filepath
        else:
            self.filepath = PHONE_CONF

    @staticmethod
    def user_phone_created(type_num, user_name, password='12345678'):
        hm = HandleMysql()
        hr = HandleRequest()
        phone_sql = hy.read_yaml('mysql', 'sql')
        phone_url = hy.read_yaml('mysql', 'url') + '/member/register'
        hr.common_head({
            "X-Lemonban-Media-Type": "lemonban.v2"
        })
        while True:
            phone_num = hm.get_noexist_phone(phone_sql)
            para_data = {
                "mobile_phone": phone_num,
                "pwd": password,
                "type": type_num,
                "reg_name": user_name
            }
            hr.send(url=phone_url, data=para_data)
            result = hm.judge_mysql_exist(phone_sql, phone_num)
            if result:
                user_id = hm.obtain_mysql_result(phone_sql, args=phone_num)[0]['id']
                break
        user_data = {user_name:
            {
                "user_id": user_id,
                "mobile_phone": phone_num,
                "type": type_num,
                "reg_name": user_name
            }
        }
        hm.close()
        hr.close()
        return user_data

    def generate_user_phone(self):
        data_phone = {}
        admin = self.user_phone_created(0, user_name='admin')
        data_phone.update(admin)
        borrower = self.user_phone_created(1, user_name='borrower')
        data_phone.update(borrower)
        investor = self.user_phone_created(1, user_name='investor')
        data_phone.update(investor)

        conf_path = HandleYaml(self.filepath)
        conf_path.write_yaml(data_phone)


if __name__ == '__main__':
    hp = HandlePhone()
    hp.generate_user_phone()
