import unittest
#应用discover执行测试套件
testdir = "./"
discover = unittest.defaultTestLoader.discover(testdir,pattern="test*.py")
runner = unittest.TextTestRunner()
runner.run(discover)