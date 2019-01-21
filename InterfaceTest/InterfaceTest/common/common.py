import xlrd
import readConfig
import os

def get_xls(xls_name,sheet_name):
     #存储表内容
     cls = []
     #获取xls文件所在的路径
     xlsPath = os.path.join(readConfig.proDir,"testfile\\cases",xls_name)
     print(xlsPath)
     #打开文件
     exlfile = xlrd.open_workbook(xlsPath)
     #获取单张表
     exlsheet = exlfile.sheet_by_name(sheet_name)
     #获取表的行数
     nrows = exlsheet.nrows
     #遍历表的内容
     for i in range(nrows):
         if exlsheet.row_values(i)[0] != "case_name":
             cls.append(exlsheet.row_values(i))
     return cls



if __name__ == "__main__":
    aa = range(0,5)
    print(list(aa))
    login = get_xls("userCase.xlsx","login")
    print(login)

