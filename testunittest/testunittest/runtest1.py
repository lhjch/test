import unittest
import HTMLTestRunner

#应用discover执行测试套件
testdir = "./"
discover = unittest.defaultTestLoader.discover(testdir,pattern="para.py")
#runner = unittest.TextTestRunner()
#runner.run(discover)

#生成测试报告
#suite = unittest.TestSuite()
#for test in discover:
    #suite.addTest(test)
#print(suite)
fp = open("fff.html","wb")
runner1 = HTMLTestRunner.HTMLTestRunner(stream=fp,title="test title",description="test description")
runner1.run(discover)