"""
Time:2019/12/18 0018
"""
import yaml
import configparser

from scripts.handle_path import YAML_PATH, CONF_PATH


class HandleYaml:

    def __init__(self, filepath):
        self.filepath = filepath

    def read_yaml(self, section_name, option_name):
        with open(self.filepath, encoding='utf8') as f:
            data_li = yaml.full_load(f)
        yaml_name = data_li[section_name][option_name]
        return yaml_name

    def write_yaml(self, json_data):
        with open(self.filepath, mode='a', encoding='utf8') as f:
            yaml.dump(json_data, f, allow_unicode=True)


hy = HandleYaml(YAML_PATH)


class HandleConfig:

    def __init__(self, filepath):
        self.filepath = filepath
        self.conf = configparser.ConfigParser()

    def read_conf(self, section_name, option_name):
        conf_li = self.conf.read(self.filepath, encoding='utf8')
        conf_data = conf_li[section_name][option_name]
        try:
            cd = eval(conf_data)
        except NameError as e:
            return conf_data
        else:
            return cd

    def write_conf(self, datas):
        for data in datas:
            self.conf[data] = datas[data]
        with open(self.filepath, mode='a', encoding='utf8') as f:
            self.conf.write(f)

hc = HandleConfig(CONF_PATH)


if __name__ == '__main__':
    data = {'admin': {'user_id': 92673, 'mobile_phone': '15201495386', 'type': 0, 'reg_name': 'admin'},
            'borrower': {'user_id': 92674, 'mobile_phone': '15246037581', 'type': 1, 'reg_name': 'borrower'},
            'investor': {'user_id': 92675, 'mobile_phone': '15212978356', 'type': 1, 'reg_name': 'investor'}}
    hy.write_yaml(json_data=data)