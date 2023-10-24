from functools import lru_cache
import sys


sys.setrecursionlimit(10000)


@lru_cache(None)
def f(n):
    if n == 1:
        return 1
    if n > 1:
        return n + f(n-1)


cnt = 0
for i in range(1, 101):
    if (f(2023)//f(i))%2==0:
        cnt += 1


print(cnt)