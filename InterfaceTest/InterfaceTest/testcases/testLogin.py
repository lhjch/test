from common.configHttp import configHttp
import unittest
import readConfig
import paramunittest
from common.excelOp import get_xls
import os

confighttpObj = configHttp()
#读取login表的内容 返回列表
logincaseContent = get_xls("complicationInterface.xlsx","login")

@paramunittest.parametrized(*logincaseContent)
class testLogin(unittest.TestCase):
    def setParameters(self,case_name,method,username,password,msg):
        self.case_name = case_name
        self.method = method
        self.username = username
        self.password = password
        self.msg = msg
        self.result =None


    @classmethod
    def setUpClass(cls):
        print("开始执行该模块用例")

    @classmethod
    def tearDownClass(cls):
        print("该模块用例执行结束")



    def test01(self):
        print("login模块中的第二条用例")


    def test_Login(self):
        #首先设置接口信息
        cookie = confighttpObj.cookie
        headers = {"Content-Type":"application/x-www-form-urlencoded","Cookie":cookie}
        url = confighttpObj.baseurl + "/allUser/signin.do"
        data = {"username":self.username,"password":self.password}
        confighttpObj.set_information(headers,None,url,data=data)
        #判断是发送post请求还是get请求
        if self.method == "get":
            self.result = confighttpObj.get()
        elif self.method == "post":
            self.result = confighttpObj.post()
        #进行断言
        self.checkResult()

    #断言
    def checkResult(self):
        resuletText = self.result.text
        self.assertEqual(resuletText,self.msg)

if __name__ == "__main__":
    unittest.main()