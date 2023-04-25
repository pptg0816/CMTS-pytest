import argparse
import configparser
import pytest
import json


def main(system_name, system_ini, extend_ini, test_cases):

    # set argumentParser for different arguments
    # the expectation in command line may looks like:
    # python run.py -name sit1 -sys system_ini -b extend_ini.ini
    parser = argparse.ArgumentParser()
    parser.add_argument("-name", "--system_name", help="system name", required=True)
    parser.add_argument("-sys", "--system_ini", help="Path to system.ini", required=True)
    parser.add_argument("-ext", "--extend_ini", help="Path to extend.ini", required=True)
    args = parser.parse_args()

    sys_ini_path = "testBed/" + args.system_name + "/" + args.system_ini
    ext_ini_path = "testBed/" + args.system_name + "/" + args.system_ini

    # read ini files
    config_sys = configparser.ConfigParser()
    config_sys.read(sys_ini_path)

    config_ext = configparser.ConfigParser()
    config_ext.read(ext_ini_path)

    # 序列化配置对象
    serialized_config_sys = json.dumps({section: dict(system_ini[section]) for section in system_ini.sections()})
    serialized_extend_ini = json.dumps({section: dict(extend_ini[section]) for section in extend_ini.sections()})

    separators = ' ,;'
    test_list = [item.strip() for item in test_cases if item not in separators]





