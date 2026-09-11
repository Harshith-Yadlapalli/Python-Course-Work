import random
ch="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ch+="abcdefghijklmnopqrstuvwxyz"
ch+="0123456789"
ch+="@#$_-"
len=int(input())
password=""
for i in range(len):
    c=random.choice(ch)
    password+=c
print(password)

#______________________________________________________________________

up="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lo="abcdefghijklmnopqrstuvwxyz"
nu="0123456789"
sp="@#$_-"
password=[]
len=int(input())
if len<4:
    print(f'Password length : {len}, Choose Password length higher')
else:
    password.append(random.choice(up))
    password.append(random.choice(lo))
    password.append(random.choice(nu))
    password.append(random.choice(sp))
for i in range(len-4):
    all=up+lo+nu+sp
    ch=random.choice(all)
    password.append(ch)
    random.shuffle(password)
n="".join(password)
print(n)