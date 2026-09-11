import Bank
# print(Bank.depost(5000))
# print(Bank.withdraw(1500))
# print(Bank.check_balane())

pin_num=int(input())
if Bank.pin==pin_num:
    print("Enter a Choice: ")
    print("1.Check Balance")
    print("2.Withdraw")
    print("3.Deposit")
    choice=input()
    if choice=="1":
        print(Bank.check_balane())
    elif choice=='2':
        print(Bank.withdraw(1500))
    elif choice=='3':
        print(Bank.depost(5000))
    else:
        print("Enter an correct choice")
else:
    print("Re enter Pin")

