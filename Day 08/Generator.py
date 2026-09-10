def gen(n):
    yield 1
    yield 2
    yield 3
    yield 4
r=gen(5)
print(next(r)) # 1
print(next(r)) # 2
print(next(r)) # 3
print(next(r)) # 4


l=[1,2,3,4,5,6]
def list():
    for i in l:
        yield 1
        yield 4
        yield 5
r=list()
print(next(r))# 1
print(next(r))# 4

def gen(x):
    x+=1
    yield x
    x+=10
    yield x
    x+=25
    yield x
m=gen(5)
print(type(m)) # <class 'generator'>
print(next(m)) # 6
print(next(m)) # 16
print(next(m)) # 41
