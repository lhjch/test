import unittest
import paramunittest
import time
from unittest import mock
import requests
import sys
import test1.readcaselist

# python3.6
# 作者：上海-悠悠

@paramunittest.parametrized(
    {"user": "admin", "psw": "123", "result": "true"},
    {"user": "admin1", "psw": "1234", "result": "true"},
    {"user": "admin2", "psw": "1234", "result": "true"},
    {"user": "admin3", "psw": "1234", "result": "true"},
    {"user": "admin4", "psw": "1234", "result": "true"},
    {"user": "admin5", "psw": "1234", "result": "true"},
    {"user": "admin6", "psw": "1234", "result": "true"},
    {"user": "admin7", "psw": "1234", "result": "true"},
    {"user": "admin8", "psw": "1234", "result": "true"},
    {"user": "admin9", "psw": "1234", "result": "true"},
    {"user": "admin10", "psw": "1234", "result": "true"},
    {"user": "admin11", "psw": "1234", "result": "true"},
)

class TestDemo(unittest.TestCase):
    def setParameters(self, user, psw, result):
        '''这里注意了，user, psw, result三个参数和前面定义的字典一一对应'''
        self.user = user
        self.psw = psw
        self.result = result
        print(self.user,self.psw,self.result)

    def testcase(self):
        print("开始执行用例：--------------")
        time.sleep(0.5)
        print("输入用户名：%s" % self.user)
        print("输入密码：%s" % self.psw)
        print("期望结果：%s " % self.result)
        time.sleep(0.5)
        self.assertTrue(self.result == "true")


@paramunittest.parametrized(
    {"user": "11", "psw": "123", "result": "true"},
    {"user": "12", "psw": "1234", "result": "true"},
    {"user": "13", "psw": "1234", "result": "true"},
    {"user": "14", "psw": "1234", "result": "true"},
)
class TestDemo1(unittest.TestCase):
    def setParameters(self, user, psw, result):
        '''这里注意了，user, psw, result三个参数和前面定义的字典一一对应'''
        self.user = user
        self.psw = psw
        self.result = result
        print(self.user,self.psw,self.result)

    def testcase(self):
        print("开始执行用例：--------------")

        print("输入用户名：%s" % self.user)
        print("输入密码：%s" % self.psw)
        print("期望结果：%s " % self.result)

        self.assertTrue(self.result == "true")


if __name__ == "__main__":
      # unittest.main()
      test1.readcaselist.readfile()

