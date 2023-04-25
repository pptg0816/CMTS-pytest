import pytest
import json
import random

@pytest.fixture(scope="session")
def system_ini(request):
    return json.loads(request.config.getoption("--system_ini"))

@pytest.fixture(scope="session")
def extend_ini(request):
    return json.loads(request.config.getoption("--extend_ini"))

def testCMsOnlineRatio(system_ini):
    CMs_expect_ratio = system_ini['section2']['CMs_expect_ratio']
    CMs_upstream_ratio = system_ini['section3']['CMs_upstream_ratio']
    real_CM_ratio = 100 * random.random()
    real_upstream_ratio = 100 * random.random()
    assert CMs_expect_ratio <= real_CM_ratio, "get too low real cm ratio"
    assert CMs_upstream_ratio <= real_upstream_ratio, "get too low ups cm ratio"


@pytest.mark.skipif(lambda: extend_ini['section1']['CMs_mac'] == '', reason="sit2 lost CM mac")
def testCMsMac(extend_ini):
    # Your test code here
    pass

def pytest_addoption(parser):
    parser.addoption("--system_ini", type=str, help="Serialized ConfigParser object from system_ini.ini")
    parser.addoption("--extend_ini", type=str, help="Serialized ConfigParser object from extend_ini.ini")


