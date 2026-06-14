def outer(num1):
    def inner(num2):
        # 1.si sans nonlocal alors on cherche une variable au sein de cette fonction et pas l autre
        nonlocal num1
        num1 += num2
        print(num1)
    return inner
#num1=10 创建了内部函数inner 并返回给fn
fn=outer(10)
# fn(10) ==> inner(10)
# 此时 num1=num2=10
#执行num1+=num2 ==> num1=20

#因为有nonlocal 修改的是闭包里的num1
#2. 没有nonlocal 那么fn(10) 一直都是一样的数值 做不到余额相加
fn(10)
fn(10)

#我们创建了一个带状态的函数，num1会一直保存在函数内部，并随着调用不断更新