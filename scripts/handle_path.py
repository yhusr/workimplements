"""
Time:2019/12/18 0018
"""
import os
import time

# 当前文件目录
abs_path = os.path.abspath(__file__)
# 获取上级目录
file_path = os.path.dirname(abs_path)
# 获取work根目录
work_path = os.path.dirname(file_path)

# 获取datas目录
data_path = os.path.join(work_path, 'datas')

# 获取excel目录
EXCEL_PATH = os.path.join(data_path, 'excelcases.xlsx')

# 获取配置文件的目录
config_file = os.path.join(work_path, 'config')
YAML_PATH = os.path.join(config_file, 'yaml_config.yaml')
CONF_PATH = os.path.join(config_file, 'conf_config.config')

# 获取日志的目录
logs_path = os.path.join(work_path, 'logs')
log_time = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
LOG_PATH = os.path.join(logs_path, f'log{log_time}.log')

# 获取phone的配置目录
PHONE_CONF = os.path.join(config_file, 'phone_config.yaml')

# 获取cases的目录
PATH_CASES = os.path.join(work_path, 'cases')

# 获取报告的地址
REPORT_PATH = os.path.join(work_path, 'reports')
