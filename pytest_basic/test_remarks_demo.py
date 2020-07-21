# -*-coding:utf-8 -*-
"""
    pytest运行时可以使用@pytest.mark.market装饰器来运行被标识的测试用例
    使用命令行运行  pytest -m slow test_remarks_demo.py

    如果要运行多个标识的话，可以使用以下表达式，如下:
        pytest -m "slow or faster"
        pytest -m "slow and faster"
        pytest -m "slow and not faster"
"""
import pytest


class TestClass(object):

    @pytest.mark.faster
    def test_one(self):
        """new_etests"""
        x = "this"
        assert 'h' in x

    @pytest.mark.faster
    @pytest.mark.slow
    def test_two(self):
        '''just a test'''
        x = "hello"
        assert hasattr(x, 'check')

    @pytest.mark.slow
    def test_three(self):
        assert 1 == 2

    def test_four(self):
        assert 2 == 3
