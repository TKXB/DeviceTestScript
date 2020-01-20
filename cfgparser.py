# -* - coding: UTF-8 -* -
import configparser


config_raw = configparser.RawConfigParser()
config_raw.read("./config.cfg")
# 读取配置文件中 [DEFAULT]
defaults = config_raw.defaults()
print(defaults)
strings = config_raw.get('DEFAULT', 'SERIAL_PATH')
print(strings)
print(type(strings))


