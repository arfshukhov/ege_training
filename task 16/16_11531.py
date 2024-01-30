import sys
from numba import njit
from functools import *
sys.setrecursionlimit(1000000)


@lru_cache(None)
def f(n):
    if n < 10:
        return n
    else:
        return f(n%10)+f(n//10)

c = 0

for i in range(1, 2**63):
    if f(i) == 159:
        c +=1

print(c)