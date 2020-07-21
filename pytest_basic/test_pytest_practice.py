# -*-coding:utf-8 -*-
"""
    参考博客:https://www.jianshu.com/p/932a4d9f78f8
    pytest基本使用
        切换到需要运行的文件目录下，运行命令行:pytest可以直接检测以test开头的文件
        pytest test_pytest_practice.py -s -n 2

"""
import pytest


def func(x):
    print("this is test data")
    return x + 1


def test_demo():
    assert func(3) == 5


if __name__ == "__main__":
    test_demo()
