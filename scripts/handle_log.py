"""
Time:2019/12/22 0022
"""
import logging

from scripts.handle_config import hy
from scripts.handle_path import LOG_PATH


class HandleLog:
    def __init__(self, filepath=None):
        if filepath:
            self.filepath = filepath
        else:
            self.filepath = LOG_PATH

    def my_log(self):
        # 设置log输入内容
        mylogger = logging.getLogger('myInterface')
        formats = logging.Formatter(hy.read_yaml('log', 'format'))
        mylogger.setLevel(hy.read_yaml('log', 'level'))

        # 设置log控制台输出
        console_handle = logging.StreamHandler()
        mylogger.setLevel(hy.read_yaml('log', 'level'))
        console_handle.setFormatter(formats)
        mylogger.addHandler(console_handle)

        # 设置file文件输出
        file_handle = logging.FileHandler(self.filepath, mode='a', encoding='utf8')
        file_handle.setFormatter(formats)
        mylogger.setLevel(hy.read_yaml('log', 'level'))
        mylogger.addHandler(file_handle)

        return mylogger


hl = HandleLog()
mylogger = hl.my_log()
if __name__ == '__main__':
    hl = HandleLog()
    mylogger = hl.my_log()
    mylogger.setLevel('DEBUG')
