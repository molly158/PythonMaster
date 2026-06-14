def outer(func):
    def inner():
        print("我要睡觉了")
        func()
        print("我起床了")
    return inner

#装饰器 decorator
#实际上执行 sleep=outer(sleep) 即 func=sleep
@outer
def sleep():
    import random
    import time
    print("sleeping...")
    time.sleep(random.randint(1,5))

sleep()