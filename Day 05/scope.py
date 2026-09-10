#  local scope
def f1():
    x = 5
    print(x)
f1()  # output: 5

# # Global scope
x = 10
def f2():
    print(x)
f2()
print(x)   # output: 10
#                    10

x=20
def f2():
    global x
    x=x+50
    print(x)
f2()
print(x)   # output: 70
#                    70

# # Enclosing scope
def f3():
    x="outer"
    def f4():
        y="inner"
        print(y)
        print(x)
    f4()
f3()      # output: inner
          #         outer

# # Built-in scope
def f5():
    a=[13,27,8,12]
    return sum(a)
print(f5())  # output: 60

# #Pass by Object Reference
def modify_number(x):
    x = x + 10  # Rebinds 'x' to a completely new integer object
    print("Inside function:", x)
num = 5
modify_number(num)
print("Outside function:", num) #output :  Inside function: 15
#                                          Outside function: 5  

# # ex2 pass by object reference
def md(x):
    x=20
    print(id(x))
    print(a)
a=10
print(id(a))
md(a)   # output: 140718551114952
#                 140718551115272
#                 20


def f(x):
    x=[10,20,30]
    print(id(x))
    print(x)
a=[13,27,30] # output:2273927585920
print(id(a)) #        2273927734144
f(a)         #        [10, 20, 30]

x=10
a=30
x=a
print(id(x)) # 140718551115592
print(id(a)) # 140718551115592

#Recursion function  of Factorial
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))  # output: 120
