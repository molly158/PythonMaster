def outer(func):
    def inner():
        print("我要睡觉了")
        func()
        print("我起床了")
    return inner

def sleep():
    import random
    import time
    print("sleeping...")
    time.sleep(random.randint(1,5))

#把函数当参数传进去
#相当于 func=sleep 返回inner
fn=outer(sleep)
#实际上执行inner()
fn()

#没有修改sleep的代码 但是却增加了功能：包装(wrap）一个函数 也是装饰器的原理