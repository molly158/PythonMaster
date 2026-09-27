#递归recursion：一个函数调用他自己
#终止条件cas de base 递归调用（appel recursif)

import os

def test_os():
    #查看文件夹里面有什么 listdir:列出目录内容
    print(os.listdir("/Users/yixueliang/PycharmProjects/PythonMaster/Chapter3"))
    #判断是否是文件夹
    print(os.path.isdir("/Users/yixueliang/PycharmProjects/PythonMaster/Chapter3"))
    #判断路径是否存在
    print(os.path.exists("/Users/yixueliang/PycharmProjects/PythonMaster/Chapter3"))
test_os()