"""

account_amount=0 #账户余额
def atm(num,deposit=True):
    global account_amount
    if deposit:
        account_amount+=num
        print(f"depots + {num},Solde du compte:{account_amount}")
    else:
        account_amount-=num
        print(f"Retraits:-{num},Solde du compte:{account_amount}")
atm(300)
atm(300)
atm(100,False)
"""

#闭包：atm虽然已经被return到外面，但仍然保存着initial_amount 这个变量
def account_create(initial_amount=0):
    #num =金额 ； deposit=True 默认存钱
    def atm(num, deposit=True):
        #修改外层函数 account_ create 中的 initial_amount
        nonlocal initial_amount
        if deposit:
            initial_amount += num
            print(f"depots + {num},Solde du compte:{initial_amount}")
        else:
            initial_amount -= num
            print(f"Retraits:-{num},Solde du compte:{initial_amount}")
    #返回的是函数本身
    return atm

#返回的是atm函数
fn=account_create(100) #fn()=atm()
fn(300)
fn(300)
fn(100,False)
