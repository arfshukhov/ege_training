m = 10000000542
from fnmatch import *

lst=[]

for i in range(m, 10**11+1, 2023):
    if fnmatch(str(i), "1*1"):
        lst.append(i)

lst.reverse()

for i in range(5):
    print(lst[i], lst[i]//2023)
