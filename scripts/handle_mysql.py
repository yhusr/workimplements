"""
Time:2019/12/22 0022
"""
import pymysql
import random

from scripts.handle_config import hy


class HandleMysql:

    def __init__(self):
        self.send_sql = pymysql.connect(
            host=hy.read_yaml('mysql', 'host'),
            user=hy.read_yaml('mysql', 'user'),
            password=hy.read_yaml('mysql', 'password'),
            port=hy.read_yaml('mysql', 'port'),
            db=hy.read_yaml('mysql', 'db'),
            charset='utf8',
            cursorclass=pymysql.cursors.DictCursor
        )
        self.my_cursor = self.send_sql.cursor()

    def obtain_mysql_result(self, sql, is_more=True, args=None):
        self.my_cursor.execute(sql, args=args)
        # 执行后必须提交才能生效
        self.send_sql.commit()
        if is_more:
            sql_result = self.my_cursor.fetchall()
        else:
            sql_result = self.my_cursor.fetchone()
        return sql_result

    @classmethod
    def random_phonenum(cls):
        return hy.read_yaml('phonenum', 'prefix') + ''.join((random.sample('0123456789', 8)))

    def judge_mysql_exist(self, sql, phone, is_more=False):
        result = self.obtain_mysql_result(sql, args=[phone], is_more=is_more)
        if result:
            return True
        else:
            return False

    def get_noexist_phone(self, sql):
        while True:
            phone = self.random_phonenum()
            exist_result = self.judge_mysql_exist(sql, phone)
            if not exist_result:
                break
        return phone

    def close(self):
        self.my_cursor.close()
        self.send_sql.close()


if __name__ == '__main__':
    hm = HandleMysql()
    phone_result = hm.judge_mysql_exist(hy.read_yaml('mysql', 'sql'), "15220489573")
    print(phone_result)
    hm.close()
