# -*-coding:utf-8 -*-
"""
    fixture scope的范围参数
之前使用@pytest.fixture(scope='module')来定义框架，scope的参数有以下几种

    function   每一个用例都执行
    class        每个类执行
    module     每个模块执行(函数形式的用例)
    session     每个session只运行一次，在自动化测试时，登录步骤可以使用该session

"""
from __future__ import print_function
import pytest


@pytest.fixture(scope='module')
def resource_a_setup(request):
    print("---now in setup scope---")
    print('\nresource_a_setup()')

    def resource_a_teardown():
        print("---now in teardown scope---")
        print('\nresource_a_teardown()')

    print("---step 1 ---")
    request.addfinalizer(resource_a_teardown)


def test_1(resource_a_setup):
    print('test_1()')


def test_2():
    print('\ntest_2()')


def test_3(resource_a_setup):
    print('\ntest_3()')


if __name__ == "__main__":
    resource_a_setup()
