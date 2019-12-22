"""
Time:2019/12/22 0022
"""
import re

class HandleRe:

    @classmethod
    def use_re(cls, no_exist_phone, data):
        if re.search('{no_exist_phone}', data):
            data = re.sub('{no_exist_phone}', no_exist_phone, data)
        return data