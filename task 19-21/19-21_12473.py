import sys


sys.setrecursionlimit(100000)

def f(m, h):
    if h >= 129:
        return m-1 % 2 == 0
    if m == 0:
        return 0
    ms = [f(m-1, h+1), f(m-1, h*2)]
    return any(ms) if (m%2)!=0 else all(ms)


for i in range(128):
    if f(2, i):
        print(i)
        break