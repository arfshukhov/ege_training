from fnmatch import *

for i in range(0, 10**10, 2023):
    r = sum(map(int, list(str(i))))
    if r == 22 and fnmatch(str(i), "1?1?1?1*1"):
        print(i)
