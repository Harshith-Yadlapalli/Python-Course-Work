balance=100000
pin=1327
def depost(amt):
    global balance
    balance+=amt
    return balance
def withdraw(amt):
    global balance
    if amt<balance:
        balance-=amt
        return balance
    return "Insufficiant funds"
def check_balane():
    return balance
def pin_generation():
    return pin