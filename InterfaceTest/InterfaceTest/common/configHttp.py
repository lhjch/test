import requests
from readConfig import readConfig
from common.log import log
localreadconfig = readConfig()

class configHttp:
    def __init__(self):
        self.baseurl = localreadconfig.get_interface("baseurl")
        self.token = localreadconfig.get_interface("token")
        self.cookie = localreadconfig.get_interface("Cookie")
        self.log = log().get_log()
        self.headers = {}
        self.data = {}

    def set_information(self,headers,params,url,data):
        self.headers = headers
        self.data = data
        self.params = params
        self.url = url


    #定义get方法
    def get(self):
        try:
            response = requests.get(self.url,params=self.params,headers=self.headers)
            return response
        except Exception as e:
            self.log.error(e)

    #定义post方法
    def post(self):
        try:
            response = requests.post(self.url,headers=self.headers,data=self.data)
            return response
        except Exception as e:
            self.log.error(e)


