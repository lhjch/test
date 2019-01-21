import requests
from readConfig import readConfig
from common.log import log
localreadconfig = readConfig()

class configHttp:
    def __init__(self):
        self.host = localreadconfig.get_http("baseurl")
        self.prot = localreadconfig.get_http("port")
        self.timeout = localreadconfig.get_http("timeout")
        self.log = log().get_log()
        self.headers = {}
        self.params = {}
        self.data = {}
        self.url = None
        self.files = {}

    def set_information(self,headers,params,url,data,files):
        self.headers = headers
        self.data = data
        self.params = params
        self.url = url
        self.files =files

    #定义get方法
    def get(self):
        try:
            response = requests.get(self.url,params=self.params,headers=self.headers,timeout=self.timeout)
            return response
        except Exception as e:
            self.log.error(e)

    #定义post方法
    def post(self):
        try:
            response = requests.post(self.url,headers=self.headers,data=self.data,
                                     files=self.files,timeout=self.timeout)
            return response
        except Exception as e:
            self.log.error(e)


