#获取根目录
import os


def getRootPath():
    rootPath = os.path.abspath(__file__)
    rootPathfile = os.path.split(rootPath)[0]
    rootPath1 = os.path.realpath(__file__)

    print(rootPath)
    print(rootPathfile)
    print(rootPath1)

    return rootPathfile





