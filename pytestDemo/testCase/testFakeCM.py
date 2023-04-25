import pytest
import json
import random


@pytest.fixture(scope="session", autouse=True)
def system_ini(request):
    return json.loads(request.config.cache.get("_system_ini", None))


@pytest.fixture(scope="session", autouse=True)
def extend_ini(request):
    return json.loads(request.config.cache.get("_extend_ini", None))


def testCMsOnlineRatio(system_ini):
    if system_ini['section1']['sit_name'] == 'sit2':
        pytest.skip("sit2 doesn't have cm info")
    CMs_expect_ratio = float(system_ini['section2']['cms_expect_ratio'])
    CMs_upstream_ratio = float(system_ini['section3']['cms_upstream_ratio'])
    real_CM_ratio = 100 * random.random()
    real_upstream_ratio = 100 * random.random()
    assert CMs_expect_ratio <= real_CM_ratio, "get too low real cm ratio." + '\n' + \
                                              "expect {} vs real {}".format(CMs_expect_ratio, real_CM_ratio)
    assert CMs_upstream_ratio <= real_upstream_ratio, "get too low ups cm ratio" + '\n' + \
                                                      "expect {} vs real {}".format(CMs_upstream_ratio, real_upstream_ratio)


def testCMsMac(extend_ini):
    print(extend_ini['section1']['cms_mac'])
    pass
