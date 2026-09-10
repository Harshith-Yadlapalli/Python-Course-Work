# without LC
l=[1,2,3,4,5]
m=[]
for i in l:
    n=i*2
    m.append(n)
print(m)

#With LC 
l=[1,2,3,4,5]
x=[i*2 for i in l]
print(x)

# LC with If-else
l=[1,2,3,4,5,6]
m=["even" if x%2==0 else "odd" for x in l]
print(m)

#loop
l=[1,2,3,4,5,6]
for i in l:
    if i%2==0:
        print("even",end=" ")
    else:
        print("Odd",end=" ")
print()

#matrix
x=1
for i in range(3):
    for j in range(3):
        print(x,end=" ")
        x+=1
    print()


m=[[1,2,3],[4,5,6],[7,8,9]]
r=[(row,col) for row in range(len(m)) for col in range( len(m[row]))]
print(r)

m=[[1,2,3],[4,5,6],[7,8,9]]
r=[(m[row][col]) for row in range(len(m)) for col in range( len(m[row]))]
print(r)

