#单独启一个线程运行log
import logging
from datetime import datetime
import threading
import readConfig
import os

class log:
    def __init__(self):
        # 创建日志目录
        proDir = readConfig.proDir
        resultpath = os.path.join(proDir, "result")
        if os.path.exists(resultpath) == False:
            os.mkdir(resultpath)
        logPath = os.path.join(resultpath,str(datetime.now().strftime("%Y%m%d%H%M%S")))
        if os.path.exists(logPath) == False:
            os.mkdir(logPath)
        # 创建一个logger
        self.logger = logging.getLogger()
        # 创建日志级别
        self.logger.setLevel(logging.INFO)
        # 创建handler 用于写入日志文件
        handler = logging.FileHandler(os.path.join(logPath, "output.log"))
        # 定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        # 给logger添加Handler
        self.logger.addHandler(handler)

    @staticmethod
    def get_log(self):
        return self.logger



if __name__ == "__main__":
    print(datetime.now())
    print(datetime.now().strftime("%Y%m%d%H%M%S"))
    aa = log()
    aa.logger.info("DDSDSDSGDSG")
    aa.logger.error("etewtew")


