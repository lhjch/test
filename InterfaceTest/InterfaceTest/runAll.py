import readConfig
import os
import unittest
import HTMLTestRunner
from common.sendMail import sendMail

proPath = readConfig.proDir
print(proPath)

class AllTest:
    def __init__(self):
        self.testsuite = []
        self.sendmail = sendMail()

    def getTestCasefile(self):
        #挑选需要执行的用例文件名称 保存在列表caselist 根据用例文件名挑选哪些用例需要执行
        caselist = []
        casefile = os.path.join(proPath,"caselist.txt")
        with open(casefile,"r") as f:
            fileContent = f.readlines()
            for case in fileContent:
                if case.startswith("#") == False:
                    caselist.append(case)

        return caselist


    def getTestSuite(self):
        print("fsafsfsa")
        casefiles = self.getTestCasefile()
        discoverlist = []
        testsuites = unittest.TestSuite()
        basedir = os.path.join(proPath,"testcases")

        for cesefile in casefiles:
            #discover为一个测试套件 需要对cesefile去掉末尾的换行符
            discover = unittest.defaultTestLoader.discover(basedir,pattern=cesefile.strip()+".py")
            #print(basedir,cesefile,discover,type(discover))
            discoverlist.append(discover)

        #组装所有的测试用例形成测试套件
        for discover in discoverlist:
            testsuites.addTest(discover)
        return testsuites

    #批量执行测试用例并发送邮件
    def runTest(self):
        testsuites = self.getTestSuite()
        # 测试报告路径
        reportPath = os.path.join(readConfig.proDir, "result", "report\\report.html")
        reportFile = open(reportPath, "wb")
        print(reportFile)
        runner = HTMLTestRunner.HTMLTestRunner(stream=reportFile, title="测试报告", description="并发症查询平台自动化测试")
        runner.run(testsuites)
        #发送邮件
        self.sendmail.sendReport()


if __name__ == "__main__":
    runallObj = AllTest()
    runallObj.runTest()

