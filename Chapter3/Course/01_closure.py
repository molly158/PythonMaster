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

def account_create(initial_amount=0):
    def atm(num, deposit=True):
        nonlocal initial_amount
        if deposit:
            initial_amount += num
            print(f"depots + {num},Solde du compte:{initial_amount}")
        else:
            initial_amount -= num
            print(f"Retraits:-{num},Solde du compte:{initial_amount}")
    return atm
fn=account_create(100)
fn(300)
fn(300)
fn(100,False)
