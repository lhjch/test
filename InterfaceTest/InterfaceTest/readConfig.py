import configparser
import os
import codecs

#获取readConfig.py文件所在的路径 为了获取项目根目录
proDir1 = os.path.realpath(__file__)
#print(proDir1)
#os.getcwd()得到的当前工作目录 如果是通过调用该模块进行执行 得到的就不是该文件的目录
proDir = os.path.split(proDir1)[0]
#print(proDir)
configpath = os.path.join(proDir,"config.ini")

class readConfig:
    def __init__(self):
        self.cf = configparser.ConfigParser()
        self.cf.read(configpath,encoding="UTF-8")

    def get_email(self,name):
        value = self.cf.get("EMAIL",name)
        return value

    def get_db(self,name):
        value = self.cf.get("DATABASES",name)
        return value

    def get_interface(self,name):
        value = self.cf.get("INTERFACE",name)
        return value

if __name__== "__main__":
    rc = readConfig();
    print(rc.get_db("username"))
    print(rc.get_email("mail_host"))