import testAdd
import testSubstract
import unittest

if __name__ == "__main__":
    #构造测试集合
    suite = unittest.TestSuite()
    suite.addTest(testAdd.TestAdd("testadd"))
    suite.addTest(testAdd.TestAdd("testadd2"))
    suite.addTest(testSubstract.TestSubtract("testsubstract"))
    suite.addTest(testSubstract.TestSubtract("testsubstract2"))

    #运行测试集合
    runner = unittest.TextTestRunner()
    runner.run(suite)





