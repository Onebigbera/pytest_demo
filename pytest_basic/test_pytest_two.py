# -*-coding:utf-8 -*-
"""
        pytest中运行模式
            pytest 文件名称 pytest test_pytest_two.py
            pytest 文件名称::测试用例类  pytest test_pytest_two.py::TestClassOne  函数的形式
            pytest 文件名称::测试用例类::测试函数  pytest test_pytest_two.py::TestClassOne::test_one  类用例的形式

        多进程运行pytest
        安装模块: pip install -U pytest-xdist
        运行模式：pytest test_se.py -n NUM   NUM为并发的进程数
        pytest test_pytest_practice.py -n 2

        在做接口测试时，有事会遇到503或短时的网络波动，导致case运行失败，而这并非是我们期望的结果，此时可以就可以通过重试运行cases的方式来解决。
        pip install -U pytest-rerunfailures

        pytest fixture
pytest支持以xUnit格式型的测试模型(setup/teardown)，但还与python自带的unittest还是有一点差别，如下

    模块形式----使用setup_module/teardown_module  
    函数形式----使用setup_function/teardown_function
    类形式----使用setup_class/teardown_class
    方法形式---使用setup_method/teardown_method


"""


class TestClassOne(object):
    def test_one(self):
        x = "this"
        print("This is test data")
        assert 't' in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, 'check')


class TestClassTwo(object):
    def test_one(self):
        x = "iphone"
        assert 'p' in x

    def test_two(self):
        x = "apple"
        assert hasattr(x, 'check')
