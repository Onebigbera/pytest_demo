# -*-coding:utf-8 -*-
"""
    Pytest模块中基本使用原则
        测试文件以test_开头
        测试类以Test开头，并且不能带有__init__方法
        测试函数以test_开头
        断言使用assert即可
"""


class TestClassDemo(object):
    def test_one(self):
        x = "this"
        assert "h" in x

    def test_two(self):
        y = "hello"
        assert hasattr(y, 'check')
