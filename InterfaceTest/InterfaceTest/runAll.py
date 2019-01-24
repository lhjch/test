import readConfig
import os
import unittest

proPath = readConfig.proDir
print(proPath)

class AllTest:
    def __init__(self):
        self.testsuite = []

    def getTestCasefile(self):
        #挑选需要执行的用例文件名称 保存在列表caselist
        caselist = []
        casefile = os.path.join(proPath,"caselist.txt")
        with open(casefile,"r") as f:
            fileContent = f.readlines()
            for case in fileContent:
                if case.startswith("#") == True:
                    caselist.append(case)


    def getTestSuite(self):
        print("fsafsfsa")
        casefiles = self.getTestCasefile()
        discoverlist = []
        basedir = os.path.join(proPath,"testcase")
        for cesefile in casefiles:
            #discover为一个测试套件
            discover = unittest.defaultTestLoader.discover(basedir,pattern=cesefile+".py")
            print(discover)
            discoverlist.append(discover)

        #组装所有的测试用例形成测试套件

if __name__ == "__main":
   obj = AllTest()
   aa = obj.getTestCasefile()
   obj.getTestSuite()