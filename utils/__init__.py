# -*- coding: utf-8 -*-
# @Time    : 2020/5/7 17:25
# @Author  : Liu Yalong
# @File    : __init__.py.py
from configparser import ConfigParser
from os import path


class BaseConfig:
    conf = ConfigParser()
    section_name = 'Config'
    file_name = 'config.conf'
    default_size = 200

    def write_config(self, top=default_size,
                     bottom=default_size,
                     left=default_size,
                     right=default_size,
                     speed=default_size):
        self.conf.add_section(self.section_name)
        self.conf.set(self.section_name, '顶部预留', str(top))
        self.conf.set(self.section_name, '底部预留', str(bottom))
        self.conf.set(self.section_name, '左侧预留', str(left))
        self.conf.set(self.section_name, '右侧预留', str(right))
        self.conf.set(self.section_name, '每秒移速', str(speed))

        with open(self.file_name, 'wt', encoding='utf-8') as f:
            self.conf.write(f)

    @property
    def is_exist(self, file_path=file_name):
        if path.exists(file_path):
            return True
        return False

    def read_config(self):
        # 2020/02/17  utf-8 -->utf-8-sig 此操作可以去除BOM
        self.conf.read(self.file_name, encoding='utf-8-sig')

        top = self.conf.getint(self.section_name, '顶部预留')
        bottom = self.conf.getint(self.section_name, '底部预留')
        left = self.conf.getint(self.section_name, '左侧预留')
        right = self.conf.getint(self.section_name, '右侧预留')
        speed = self.conf.getint(self.section_name, '每秒移速')

        return top, bottom, left, right, speed


if __name__ == '__main__':
    config = BaseConfig()
    if not config.is_exist:
        config.write_config()
    print(config.read_config())
