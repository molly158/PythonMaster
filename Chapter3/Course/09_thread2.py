#多线程：一个程序里同时运行多个线程（thread），让多个任务看起来能够同时执行

#process进程（程序）：一家餐厅

#餐厅（一个进程）：服务员A（线程1），服务员B（线程2），洗碗工，厨师....
#线程的特点：共享同一块内存，所以通信方便
#为什么需要多线程？例如下载文件，如果不用多线程：下载A => 下载B => 下载C （9s，3s/chacun）
#多线程=>3s 同时开始 效率++++


import threading
import time

def sing():
    while True:
        print("我在唱歌")
        time.sleep(1)

def dance(message):
    while True:
        print(message)
        time.sleep(1)

#两个线程一起进行
sing_thread = threading.Thread(target=sing)
#kw=keyword
dance_thread = threading.Thread(target=dance,kwargs={"message":"我在跳舞"})

sing_thread.start()
dance_thread.start()

#ccl:可以看到两个任务同时执行