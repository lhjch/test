import getRootpath
import os

rootpath = getRootpath.getRootPath()

caselistfliepath = os.path.join(rootpath,"caselist.txt")

def readfile():
    fileContent = open(caselistfliepath, "r")
    print(fileContent.read())
    print(type(fileContent.read()))
    fileContent.close()

    fileContent = open(caselistfliepath, "r")
    print("---------------------")
    aa = fileContent.readline()
    print(aa)
    print(type(aa))
    fileContent.close()
    print("---------------------")

    fileContent = open(caselistfliepath, "r")
    bb = fileContent.readlines()
    print(type(bb))
    print(bb)
    fileContent.close()
    for i in bb:
        print(i)

    print("++++++++++++++++++++++++")
    with open(caselistfliepath, "r") as f:
        print(f.read())


