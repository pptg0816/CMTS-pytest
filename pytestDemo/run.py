import argparse
import configparser
import pytest
import os
import json
import re


# define plugin custom class for system_ini and extend_ini
class CustomConfig:
    def __init__(self, system_ini, extend_ini):
        self.system_ini = system_ini
        self.extend_ini = extend_ini

    def pytest_addoption(self, parser):
        parser.addoption("--system_ini", type=str, help="Path to system.ini file")
        parser.addoption("--extend_ini", type=str, help="Path to extend.ini file")

    def pytest_configure(self, config):
        config._system_ini = self.system_ini
        config._extend_ini = self.extend_ini

    def pytest_sessionstart(self, session):
        session.config.cache.set("_system_ini", self.system_ini)
        session.config.cache.set("_extend_ini", self.extend_ini)


# set argumentParser for different arguments
# the expectation in command line may look like:
# python3 run.py -name sit1 -sys sit1.ini -ext sit1_CMs_mac.ini -test testFakeCM.py,tesFakeRPD.py
parser = argparse.ArgumentParser()
parser.add_argument("-name", "--system_name", help="system name", required=True)
parser.add_argument("-sys", "--system_ini", help="Path to system.ini", required=True)
parser.add_argument("-ext", "--extend_ini", help="Path to extend.ini", required=True)
parser.add_argument("-test", "--test_case", help="test list", required=True)
args = parser.parse_args()


def getPathAndReadIni(system_name, ini_name):
    ini_path = "testBed/" + system_name + "/" + ini_name
    print(ini_path)
    if not os.path.exists(ini_path):
        raise FileNotFoundError(f"file {ini_path} doesn't exist")
    else:
        ini_content = configparser.ConfigParser()
        ini_content.read(ini_path)
        serialized_ini = json.dumps({section: dict(ini_content[section]) for section in ini_content.sections()})
        print(serialized_ini)
        print(type(serialized_ini))
    return serialized_ini


# get serialized ini files' contents
serialized_system = getPathAndReadIni(args.system_name, args.system_ini)
serialized_extend = getPathAndReadIni(args.system_name, args.extend_ini)

# get test cases as a list
test_case = args.test_case
print(test_case)

# spilt the test cases by ,;" "
separators = ' ,;'
test_list = re.split(r'[;, ]', test_case)
print(test_list)

# set custom arguments
custom_config = CustomConfig(serialized_system, serialized_extend)

# run each test case on by one
for test in test_list:
    pytest.main(['-vs', f'testCase/{test}'], plugins=[custom_config])
