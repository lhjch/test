import pymssql
from readConfig import readConfig
rc = readConfig()

class databaseOp:
    def __init__(self):
    #读取数据库相关信息
     self.host = rc.get_db("host")
     self.username = rc.get_db("username")
     self.password = rc.get_db("password")
     self.port = rc.get_db("port")
     self.databasename = rc.get_db("databasename")
     self.conn = None

    #连接数据库
    def getconnect(self):
        self.conn = pymssql.connect(self.host,self.username,self.password,self.databasename)
        cur = self.conn.cursor()
        if not cur:
            raise (NameError,"连接数据库失败")
        return cur


    #查询数据库内容
    def query(self,operationContent):
        cur = self.getconnect()
        cur.execute(operationContent)
        reslist = cur.fetchall()

        return reslist

    #向数据库中增加内容
    def insert(self,operationContent):
        pass

    #修改数据库内容
    def modify(self,operationContent):
        pass

    #删除数据库中内容
    def delete(self,operationContent):
        pass

    #关闭连接
    def close(self):
        self.conn.close()


if __name__ == "__main__":
    # host = rc.get_db("host")
    # username = rc.get_db("username")
    # password = rc.get_db("password")
    # databasename = rc.get_db("databasename")

    ms = databaseOp()
    querysentence = "select * from basic_check_items where dataTypeName='非药医嘱'"
    res = ms.query(querysentence)
    print(res)
    ms.close()



