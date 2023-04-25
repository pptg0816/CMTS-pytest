import pytest
import json
import random


@pytest.fixture(scope="session", autouse=True)
def system_ini(request):
    return json.loads(request.config.cache.get("_system_ini", None))


@pytest.fixture(scope="session", autouse=True)
def extend_ini(request):
    return json.loads(request.config.cache.get("_extend_ini", None))


def testRPDnode(system_ini):
    if system_ini['section1']['sit_name'] == 'sit1':
        pytest.skip("sit1 doesn't have rpd info")
    get_rpd_node_list = system_ini['section2']['rpd_node'].split(",")
    rpd_set = set(get_rpd_node_list)
    print(rpd_set)
    random_seed = 100*random.random()
    if random_seed <= 33:
        real_rpd_set = {'1'}
    elif 33 < random_seed <= 66:
        real_rpd_set = {'1', '2'}
    else:
        real_rpd_set = {'1', '2', '3'}
    print(real_rpd_set)
    assert rpd_set == real_rpd_set, "get too low real cm ratio." + '\n' + \
                                              "expect {} vs real {}".format(rpd_set, real_rpd_set)


