import math
import random
import sys
import platform
import collections
import itertools
import datetime

# print(math.sqrt(5)) #2.236
# print(math.pow(5,2)) # 25.0
# print(math.factorial(5)) # 120
# print(math.floor(5.9)) # 5
# print(math.ceil(6.0)) # 6
# print(math.pi*5.6) # 17.59
# print(math.sin(90)) # 0.8939
# print(math.cos(120)) # 0.814
# print(math.tan(75)) # -0.4207

# radius=5
# area = math.pi*math.pow(radius,2)
# print (area) # 78.539...

# n=[10,32,14,54,10,42]
# m=["der", "fes", "br","ted"]
# print(random.random()) # 0.76843
# print(random.randint(2,9)) # 2
# print(random.choice(n)) # 10
# print(random.choices(n,k=3)) # [10,10,14]
# print(random.sample(n,k=4)) # [10,54,42,14]
# print(random.shuffle(m)) # None
# print(m) # ['ted','der', 'br','fes']


# print(sys.version) # 3.13.15...
# print(sys.platform)
# print(sys.path) ['c:\\users\\....']


# print(platform.system()) # Windows
# print(platform.release()) # 11
# print(platform.machine()) # AMD64
# print(platform.processor()) # AMD64 Family 25 Model 80 Stepping 0, AuthenticAMD
# print(platform.python_version()) # 3.13.15


# from collections import Counter

# n="Sreeyah"
# h=Counter(n)
# print(h) # Counter({'e':2, 's':1, 'r': 1, 'y':1,'a':1, 'h':1})
# nums=[1,3,2,4,5,2,5,2]
# m=Counter(nums)
# print(m) #Counter({2: 3, 5: 2, 1: 1, 3: 1, 4: 1})

# from collections import defaultdict

# d=defaultdict(int)
# d["sreeyah"]=1
# print(d["name"]) # 0
# dic={'s':2, 'h':5, 'a': 3}
# print(dic['s']) # 2
# print(dic['b']) # Error

# from collections import deque
# d=deque([13,21,34,32])
# d.append(32)
# d.appendleft(21)
# d.pop()
# d.popleft()
# print(d) #deque([13,21,34,32]) 

# from itertools import permutations
# n=[1,2,3,4]
# print(list(permutations(n,3)))

# from itertools import combinations
# n=[1,2,3,4]
# print(list(combinations(n,2)))

# from itertools import product
# a=[1,2,4]
# b=['a','b','c']
# print(list(product(a,b))) #[(1,'a'),(1,'b'),(1,'c'),....(4,'c')]

# from datetime import datetime
# n=datetime.now()
# print(n) # 2026-09-10 17:42:21.1009
# print()
# print(n.year) # 2026
# print(n.month) # 9
# print(n.date()) # 2026-09-10
# print(n.day) # 10
# print()
# print(n.hour) # 17
# print(n.minute) # 42
# print(n.second) # 21

# from datetime import date,timedelta
# t=date.today()
# f=t+timedelta(days=45)
# print(f)

from datetime import datetime
now = datetime.now()
print(now.strftime( "%H :%M :%S"))
print(now.strftime("%d/%m/%Y"))
print(now.strftime( "%d -%m-%Y"))