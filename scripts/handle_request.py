"""
Time:2019/12/22 0022
"""
import requests
import json

class HandleRequest:

    def __init__(self):
        self.one_session = requests.session()

    def common_head(self, head):
        self.one_session.headers.update(head)

    def send(self, url, method='post', data=None, is_json=True, **kwargs):
        if isinstance(data, str):
            try:
                para_data = json.loads(data)
            except NameError as n:
                data = eval(data)
            else:
                data = para_data

        method = method.lower()
        if method=='get':
            res = self.one_session.request(method, url, params=data, **kwargs)
        elif method in ('post', 'delete', 'put', 'patch'):
            if is_json:
                res = self.one_session.request(method, url, json=data, **kwargs)
            else:
                res = self.one_session.request(method, url, data=data, **kwargs)
        else:
            res = None
            print(f'此{method}方法没有返回内容')
        return res

    def close(self):
        self.one_session.close()
